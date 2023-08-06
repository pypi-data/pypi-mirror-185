"""
Copyright 2021 Objectiv B.V.
"""
import base64
import os
import re
from typing import List, Union, Dict, Tuple, Optional, cast, Any

import bach
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from modelhub.aggregate import Aggregate
from modelhub.map import Map
from modelhub.models.logistic_regression import LogisticRegression
from modelhub.models.funnel_discovery import FunnelDiscovery
from modelhub.series.series_objectiv import MetaBase
from modelhub.series import SeriesLocationStack
from sql_models.constants import NotSet
from sql_models.util import is_bigquery, is_athena


GroupByType = Union[List[Union[str, bach.Series]], str, bach.Series, NotSet]
ConversionEventDefinitionType = Tuple[Optional['SeriesLocationStack'], Optional[str]]

TIME_DEFAULT_FORMAT = '%Y-%m-%d %H:%M:%S.%f'
SESSION_GAP_DEFAULT_SECONDS = 1800


class ModelHub:
    """
    The model hub contains collection of data models and convenience functions that you can take, combine and
    run on Bach data frames to quickly build highly specific model stacks for product analysis and
    exploration.
    It includes models for a wide range of typical product analytics use cases.

    All models from the model hub can run on Bach DataFrames that contain data collected by the Objectiv
    tracker. To instantiate a DataFrame with Objectiv data use :py:meth:`get_objectiv_dataframe`. Models
    from the model hub assume that at least the columns of a DataFrame instantiated with this method are
    available in order to run properly. These columns are:

    The model hub has three main type of functions: helper functions, aggregation models and
    machine learning models.

    * Helper functions always return a series with the same shape and index as the DataFrame they originate
      from. This ensures they can be added as a column to that DataFrame. The helper functions can be accessed
      with the :py:attr:`map` accessor from a model hub instance.
    * Aggregation models return aggregated data in some form from the DataFrame. The aggregation models can be
      accessed with the :py:attr:`agg` or :py:attr:`aggregate` accessor from a model hub instance.
    * Machine learning models can be instantiated from the modelhub directly using the model's name,
      i.e. : :py:meth:`get_logistic_regression`.
    """
    def __init__(self,
                 time_aggregation: str = TIME_DEFAULT_FORMAT,
                 global_contexts: Optional[List[str]] = None):
        """
        Constructor

        :param time_aggregation: Time aggregation used for aggregation models.
        :param global_contexts: The global contexts that should be made available for analysis
        """

        self._time_aggregation = time_aggregation
        self._conversion_events = cast(Dict[str, ConversionEventDefinitionType], {})
        self._global_contexts = global_contexts or []

        # init metabase
        self._metabase = None

    @property
    def time_aggregation(self):
        """
        Time aggregation used for aggregation models, set when object is instantiated.
        """
        return self._time_aggregation

    @property
    def conversion_events(self):
        """
        Dictionary of all events that are labeled as conversion.

        Set with :py:meth:`add_conversion_event`
        """
        return self._conversion_events

    @staticmethod
    def _get_db_engine(db_url: Optional[str],
                       bq_credentials_path: Optional[str] = None,
                       bq_credentials: Optional[str] = None) -> Engine:
        """
        returns db_connection based on db_url.

        If db_url is for BigQuery, bq_credentials_path or bq_credentials can be provided.
        When both are given, bq_credentials wins.
        """
        kwargs: Dict[str, Any] = {}

        if db_url and re.match(r'^bigquery://.+', db_url):
            if bq_credentials:
                credentials_base64 = base64.b64encode(bq_credentials.encode('utf-8'))
                kwargs['credentials_base64'] = credentials_base64
            elif bq_credentials_path:
                kwargs['credentials_path'] = bq_credentials_path

        db_url = db_url or os.environ.get('DSN', 'postgresql://objectiv:@localhost:5432/objectiv')
        return create_engine(db_url, **kwargs)

    def get_objectiv_dataframe(
        self,
        *,
        db_url: str = None,
        table_name: str = None,
        start_date: str = None,
        end_date: str = None,
        bq_credentials_path: Optional[str] = None,
        bq_credentials: Optional[str] = None,
        with_sessionized_data: bool = True,
        session_gap_seconds: int = SESSION_GAP_DEFAULT_SECONDS,
        identity_resolution: Optional[str] = None,
        anonymize_unidentified_users: bool = True
    ):
        """
        Sets data from sql table into an :py:class:`bach.DataFrame` object.

        The created DataFrame points to where the data is stored in the sql database, makes several
        transformations and sets the right data types for all columns. As such, the models from the model hub
        can be applied to a DataFrame created with this method.

        For all databases, except BigQuery, the credentials can be specified as part of `db_url`. For
        BigQuery the credentials can be set with either `bq_credentials` (primary) or `bq_credentials_path`.
        Additionally, for all databases it's possible to specify credentials as part of the environment,
        either as variables, files, or some other method. For more information on specifying the credentials
        as part of the environment, check the documentation of the specific database vendor:
        `Athena
        <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials>`__
        , `BigQuery <https://cloud.google.com/docs/authentication/provide-credentials-adc>`__
        , or `Postgres <https://www.postgresql.org/docs/current/libpq-envars.html>`__.


        :param db_url: the url that indicate database dialect and connection arguments. If not given, env DSN
            is used to create one. If that's not there, the default of
            'postgresql://objectiv:@localhost:5432/objectiv' will be used.
        :param table_name: the name of the sql table where the data is stored. Will default to 'events' for
            bigquery and 'data' for other engines.
        :param start_date: first date for which data is loaded to the DataFrame. If None, data is loaded from
            the first date in the sql table. Format as 'YYYY-MM-DD'.
        :param end_date: last date for which data is loaded to the DataFrame. If None, data is loaded up to
            and including the last date in the sql table. Format as 'YYYY-MM-DD'.
        :param bq_credentials_path: optional path to file with BigQuery credentials.
        :param bq_credentials: optional BigQuery credentials, content from credentials file.
        :param with_sessionized_data: Indicates if DataFrame must include `session_id`
            and `session_hit_number` calculated series.
        :param session_gap_seconds: Amount of seconds to be use for identifying if events were triggered
            or not during the same session.
        :param identity_resolution: Identity id to be used for identifying users based on IdentityContext.
            If no value is provided, then the user_id series will contain the value from
            the cookie_id column (a UUID).
        :param anonymize_unidentified_users: Indicates if unidentified users are required to be anonymized
            by setting user_id value to NULL. Otherwise, original UUID value from the cookie will remain.

        :returns: :py:class:`bach.DataFrame` with Objectiv data.


        .. note::
            DataFrame will always include:

            .. list-table:: Objectiv DataFrame
                :header-rows: 1

                * - Series
                  - Dtype
                * - event_id
                  - uuid
                * - day
                  - date
                * - moment
                  - timestamp
                * - user_id
                  - uuid (string if identity resolution is applied)
                * - global_contexts
                  - objectiv_global_context
                * - location_stack
                  - objectiv_location_stack
                * - stack_event_types
                  - json

        .. note::
            If `with_sessionized_data` is True, Objectiv data will include `session_id` (int64)
                and `session_hit_number` (int64) series.
        """
        engine = self._get_db_engine(
            db_url=db_url, bq_credentials_path=bq_credentials_path, bq_credentials=bq_credentials
        )
        from modelhub.pipelines.util import get_objectiv_data
        if table_name is None:
            if is_athena(engine) or is_bigquery(engine):
                table_name = 'events'
            else:
                table_name = 'data'

        data = get_objectiv_data(
            engine=engine,
            table_name=table_name,
            start_date=start_date,
            end_date=end_date,
            with_sessionized_data=with_sessionized_data,
            session_gap_seconds=session_gap_seconds,
            identity_resolution=identity_resolution,
            anonymize_unidentified_users=anonymize_unidentified_users,
            global_contexts=self._global_contexts
        )

        # get_objectiv_data returns both series as bach.SeriesJson.
        data['location_stack'] = data.location_stack.astype('objectiv_location_stack')
        return data

    def add_conversion_event(self,
                             location_stack: 'SeriesLocationStack' = None,
                             event_type: str = None,
                             name: str = None):
        """
        Label events that are used as conversions. All labeled conversion events are set in
        :py:attr:`conversion_events`.

        :param location_stack: the location stack that is labeled as conversion. Can be any slice in of a
            :py:class:`modelhub.SeriesLocationStack` type column. Optionally use in conjunction with
            ``event_type`` to label a conversion.
        :param event_type: the event type that is labeled as conversion. Optionally use in conjunction with
            ``objectiv_location_stack`` to label a conversion.
        :param name: the name to use for the labeled conversion event. If None it will use 'conversion_#',
            where # is the number of the added conversion.
        """

        if location_stack is None and event_type is None:
            raise ValueError('At least one of conversion_stack or conversion_event should be set.')

        if not name:
            name = f'conversion_{len(self._conversion_events) + 1}'

        self._conversion_events[name] = location_stack, event_type

    def time_agg(self, data: bach.DataFrame, time_aggregation: str = None) -> bach.SeriesString:
        """
        Formats the moment column in the DataFrame, returns a SeriesString.

        Can be used to aggregate to different time intervals, ie day, month etc.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param time_aggregation: if None, it uses :py:attr:`time_aggregation` set from the
            ModelHub. Use any template for aggregation based on 1989 C standard format codes:
            https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
            ie. ``time_aggregation=='%Y-%m-%d'`` aggregates by date.
        :returns: SeriesString.
        """

        time_aggregation = self.time_aggregation if time_aggregation is None else time_aggregation
        return data.moment.dt.strftime(time_aggregation).copy_override(name='time_aggregation')

    _metabase: Union[None, MetaBase] = None

    def to_metabase(self, data, model_type: str = None, config: dict = None):
        """
        Plot data in ``data`` to Metabase. If a card already exists, it will be updated. If ``data`` is a
        :py:class:`bach.Series`, it will call :py:meth:`bach.Series.to_frame`.

        Default options can be overridden using the config dictionary.

        :param data: :py:class:`bach.DataFrame` or :py:class:`bach.Series` to push to MetaBase.
        :param model_type: Preset output to Metabase for a specific model. eg, 'unique_users'
        :param config: Override default config options for the graph to be added/updated in Metabase.
        """
        if not self._metabase:
            self._metabase = MetaBase()
        return self._metabase.to_metabase(data, model_type, config)

    @property
    def map(self):
        """
        Access map methods from the model hub.

        .. autoclass:: Map
            :members:
            :noindex:

        """

        return Map(self)

    @property
    def agg(self):
        """
        Access aggregation methods from the model hub. Same as :py:attr:`aggregate`.

        .. autoclass:: Aggregate
            :members:
            :noindex:

        """

        return Aggregate(self)

    @property
    def aggregate(self):
        """
        Access aggregation methods from the model hub. Same as :py:attr:`agg`.

        .. autoclass:: Aggregate
            :members:
            :noindex:

        """
        return Aggregate(self)

    def get_logistic_regression(self, *args, **kwargs) -> LogisticRegression:
        """
        Return an instance of the :py:class:`modelhub.LogisticRegression` class from the model hub.

        All parameters passed to this function are passed to the constructor of the LogisticRegression
        model.
        """

        return LogisticRegression(*args, **kwargs)

    def get_funnel_discovery(self) -> FunnelDiscovery:
        """
        Return an instance of the :py:class:`modelhub.FunnelDiscovery` class from the model hub.
        """

        return FunnelDiscovery()

    def visualize_location_stack(self,
                                 data: bach.DataFrame,
                                 root_location: str = None,
                                 location_stack: Union[str, 'SeriesLocationStack'] = None,
                                 n_top_examples=40,
                                 return_df: bool = False,
                                 show: bool = True):
        """
        Shows the location stack as a sankey chart per element for the selected root location. It shows the
        different elements by type and id as nodes from left to right. The size of the nodes and links
        indicate the number of events that have this location element or these location element combinations.

        :param data: :py:class:`bach.DataFrame` to apply the method on.
        :param root_location: the name of the root location to use for visualization of the location stack.
            If None, it will use the most common root location in the data.
        :param location_stack: the column of which to create the paths. Can be a string of the name of a
            SeriesLocationStack type column, or a Series with the same base node as `data`. If None the
            default location stack is taken.
        :param n_top_examples: number of top examples  from the location stack to plot (if we have
            too many examples to plot it can slow down the browser).
        :param return_df: returns a :py:class:`bach.DataFrame` with the data from which the sankey diagram is
            created.
        :param show: if True, it shows the plot, if False it only returns the DataFrame with the data that
            is to be plotted.

        :returns: None or DataFrame
        """

        from modelhub.util import check_objectiv_dataframe

        columns_to_check = ['user_id', 'event_id']
        if location_stack is None:
            columns_to_check = ['location_stack', 'user_id', 'event_id']
            location_stack = 'location_stack'
        check_objectiv_dataframe(df=data, columns_to_check=columns_to_check)

        if type(location_stack) == str:
            location_stack_series = data[location_stack]
        if type(location_stack) == SeriesLocationStack:
            location_stack_series = location_stack

        column = cast(SeriesLocationStack, location_stack_series)  # help mypy

        data_cp = data.copy()
        result_item, result_offset = column.json.flatten_array()

        result_item_df = result_item.sort_by_series(
            by=[result_offset]
        ).to_frame()

        result_item_df = result_item_df.rename(columns={result_item.name: '__location_stack_exploded'})

        result_item_df['__result_offset'] = 1
        result_item_df['__result_offset'] = result_item_df['__result_offset'].copy_override(
            expression=result_item_df.order_by[0].expression)

        data_merged = data_cp.merge(result_item_df, left_index=True, right_index=True)
        data_merged['__type'] = data_merged['__location_stack_exploded'].ls[
            '_type'].astype('string')
        data_merged['__id'] = data_merged['__location_stack_exploded'].ls[
            'id'].astype('string')
        data_merged['__name'] = data_merged['__type'] + ": " + data_merged['__id']

        root_location_type = "RootLocationContext"
        if root_location is None:
            root_location_data = data_merged[data_merged['__result_offset'] == 0].groupby(
                ['__type', '__id']).user_id.count().sort_values(
                ascending=False).head()
            root_location_type = root_location_data.index[0][0].strip('"')
            root_location = root_location_data.index[0][1].strip('"')

        data_merged[
            'root_location'] = data_merged.location_stack.ls.get_from_context_with_type_series(
            type=root_location_type, key='id')

        data_merged_cp = data_merged[
            data_merged.root_location == root_location].copy().reset_index()

        funnel = FunnelDiscovery()
        funnel_df = funnel.get_navigation_paths(data_merged_cp, steps=2, by='event_id',
                                                location_stack='__name', sort_by='__result_offset')

        result = funnel.plot_sankey_diagram(funnel_df, n_top_examples=n_top_examples, show=show)

        if return_df:
            return result
