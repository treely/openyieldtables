# Data Model

The `openyieldtables` library uses [pydantic](https://docs.pydantic.dev/latest/) to model the data structure.

## Raw Data

The underlying data is structured in a way that allows for easy access. The raw data is stored in CSV files and is loaded into the library using the provided [models](data_model.md#models).

The CSV files are structured as follows:

* `yield_tables_meta.csv`: Contains metadata about the available yield tables.
    - `id`: {{ yield_tables_meta.id }}
    - `title`: {{ yield_tables_meta.title }}
    - `country_codes`: {{ yield_tables_meta.country_codes }}
    - `type`: {{ yield_tables_meta.type }}
    - `source`: {{ yield_tables_meta.source }}
    - `link`: {{ yield_tables_meta.link }}
    - `yield_class_step`: {{ yield_tables_meta.yield_class_step }}
    - `age_step`: {{ yield_tables_meta.age_step }}
    - `tree_type`: {{ yield_tables_meta.tree_type }}

* `yield_tables.csv`: Contains the yield tables.
    - `id`: {{ yield_tables.id }}
    - `yield_class`: {{ yield_tables.yield_class }}
    - `age`: {{ yield_tables.age }}
    - `dominant_height`: {{ yield_tables.dominant_height }}
    - `average_height`: {{ yield_tables.average_height }}
    - `dbh`: {{ yield_tables.dbh }}
    - `taper`: {{ yield_tables.taper }}
    - `trees_per_ha`: {{ yield_tables.trees_per_ha }}
    - `basal_area`: {{ yield_tables.basal_area }}
    - `volume_per_ha`: {{ yield_tables.volume_per_ha }}
    - `average_annual_age_increment`: {{ yield_tables.average_annual_age_increment }}
    - `total_growth_performance`: {{ yield_tables.total_growth_performance }}
    - `current_annual_increment`: {{ yield_tables.current_annual_increment }}
    - `mean_annual_increment`: {{ yield_tables.mean_annual_increment }}

## Models

:::openyieldtables.models.yieldtable.YieldTableMeta
    options:
      heading_level: 3

:::openyieldtables.models.yieldtable.YieldClassRow
    options:
      heading_level: 3

:::openyieldtables.models.yieldtable.YieldClass
    options:
      heading_level: 3

:::openyieldtables.models.yieldtable.YieldTableData
    options:
      heading_level: 3

:::openyieldtables.models.yieldtable.YieldTable
    options:
      heading_level: 3
