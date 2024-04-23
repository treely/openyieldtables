# Functions

:::openyieldtables.yieldtables
    options:
      heading_level: 2
      show_root_full_path: true
      show_source: false

## Usage

**Get the metadata of all available yield tables**

```python
from openyieldtables.yieldtables import get_yield_tables_meta

# Get the metadata of all available yield tables
yield_tables_meta = get_yield_tables_meta() # Returns a list of `YieldTableMeta` objects

# Get the first yield table as dictionary
yield_table_meta = yield_tables_meta[0].model_dump()
#> {'id': 1, 'title': 'Fichte Hochgebirge', 'country_codes': ['AT', 'DE'],...}
```

**Get the metadata of one specific yield table**

```python
from openyieldtables.yieldtables import get_yield_table_meta

# Get the metadata of a yield table by its ID
yield_table_meta = get_yield_table_meta(1) # Returns a `YieldTableMeta` object

# Get the yield table metadata as dictionary
yield_table_meta_dict = yield_table_meta.model_dump()
#> {'id': 1, 'title': 'Fichte Hochgebirge', 'country_codes': ['AT', 'DE'],...}
```

**Get the data of one specific yield table**

```python
from openyieldtables.yieldtables import get_yield_table

# Get the data of a yield table by its ID
yield_table_data = get_yield_table(1) # Returns a `YieldTable` object

# Get one row of the yield table data as dictionary
yield_table_data.data[0].yield_classes[0].rows[0].model_dump()
#> {'age': 20, 'dominant_height': 5.9, 'average_height': 5.3, 'dbh': 11.5, 'taper': 0.396,...}
```
