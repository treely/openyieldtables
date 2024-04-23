<img src="https://cdn.tree.ly/assets/v4/yield-tables/logo_white_background.svg" alt="Yield Tables logo" width="280"/>

[![PyPI - Version](https://img.shields.io/pypi/v/openyieldtables)](https://pypi.org/project/openyieldtables/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/openyieldtables)](https://pypi.org/project/openyieldtables/) ![Test](https://github.com/github/docs/actions/workflows/test.yml/badge.svg) [![Documentation Status](https://readthedocs.org/projects/openyieldtables/badge/?version=latest)](https://openyieldtables.readthedocs.io/en/latest/?badge=latest)

An open source Python library for yield tables.

## Quickstart

Download the latest version of the library from [PyPI](https://pypi.org/project/openyieldtables/):

```bash
pip install openyieldtables
```

Import the library and load a yield table:

```python
from openyieldtables.yieldtables import (
    get_yield_table,
    get_yield_tables_meta,
)

# Get the metadata of all available yield tables
yield_tables_meta = get_yield_tables_meta()

# Get the data of a yield table by its ID
yield_table_data = get_yield_table(1)
```

## Documentation

You can find the documentation
[here](https://openyieldtables.readthedocs.io/en/latest/).

## Contributing

We are happy about every contribution! Please follow our
[contribution guideline](https://github.com/treely/openyieldtables/blob/main/CONTRIBUTING.md).

## About

`openyieldtables` is maintained by [Tree.ly](https://tree.ly) and
[FMM](https://www.fmm.at/).
