# Objectiv open model hub

The [open model hub](https://objectiv.io/docs/modeling/open-model-hub/) is a library of pre-built analytics models & functions to build & run deep analyses for a wide range of product & marketing use cases. It’s part of [Objectiv](https://objectiv.io/), an open-source data collection & modeling platform that helps data teams run product analytics from their notebooks. All models & operations can run directly on a full dataset collected with the Objectiv Tracker without cleaning or transformation, as the data adheres to the [strict event typing & validation of an open taxonomy](https://objectiv.io/docs/taxonomy/).

Under the hood, the open model hub is powered by [Bach](https://pypi.org/project/objectiv-bach/), a Python-based analytics modeling library with a Pandas-like interface. Bach translates all operations and models to SQL, running directly on your full dataset. All DataFrames & models can be converted to an SQL statement with just a single command, to use in other tools like dbt or BI.


## Installation

```pip install objectiv-modelhub```

See how to [get started in your notebook](https://objectiv.io/docs/modeling/get-started-in-your-notebook/) for detailed installation instructions.

## Usage

* [Example notebooks with instructions](https://objectiv.io/docs/modeling/example-notebooks/)
* [Open Model Hub API reference](https://objectiv.io/docs/modeling/open-model-hub/api-reference/
)

## Support
* [Visit Objectiv Docs for instructions & FAQs](https://objectiv.io/docs/)
* [Join Objectiv on Slack to get help](https://objectiv.io/join-slack/)
* [Request a feature or report an issue on Github](https://github.com/objectiv/objectiv-analytics)

**Found a security issue?**
Please don’t use the issue tracker but contact us directly. See [SECURITY.md](../SECURITY.md) for details.

## Contributing

If you want to contribute to the open model hub or use it as a base for custom development, take a look at [CONTRIBUTING.md](CONTRIBUTING.md) for detailed development instructions. For more unformation about our contribution process and where you can fit in, check out our [Contribution Guide](https://objectiv.io/docs/home/the-project/contribute) in the Docs.

## License

This repository is part of the source code for Objectiv, which is released under the Apache 2.0 License. Please refer to [LICENSE.md](../LICENSE.md) for details.

---

Copyright (c) 2021-2022 Objectiv B.V. All rights reserved.