# 🌲 openyieldtables

An open source Python library for yield tables.

## Quickstart

Download the latest version of the library from PyPI:

```bash
pip install openyieldtables
```

Import the library and load a yield table:

```python
from openyieldtables.yieldtables import (
    get_yield_table_data,
    get_yield_tables_meta,
)

# Get the metadata of all available yield tables
yield_tables_meta = get_yield_tables_meta()

# Get the data of a yield table by its ID
yield_table = get_yield_table(1)
```

## Documentation

You can find the documentation [here](https://openyieldtables.readthedocs.io/latest/).

## Contributing

We are happy about every contribution! Please follow our 
contribution guideline](https://github.com/treely/openyieldtables/blob/main/CONTRIBUTING.md).

## About

`openyieldtables` is maintained by [Tree.ly](https://tree.ly) and [FMM](https://www.fmm.at/).
