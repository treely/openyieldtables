# openyieldtables

The `openyieldtables` library is an open source Python library for yield tables.

## Getting Started

Download the latest version of the library from PyPI:

```bash
pip install openyieldtables
```

### Usage

Import the library and load a yield table:

```python
from openyieldtables.yieldtables import (
    get_yield_table_data,
    get_yield_tables_meta,
)

# Get the metadata of all available yield tables
yield_tables_meta = get_yield_tables_meta() # Returns a list of `YieldTableMeta` objects

# Get the data of a yield table by its ID
yield_table = get_yield_table(1) # Returns a `YieldTable` object
```
