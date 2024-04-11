# Data Model

The `openyieldtables` library uses [pydantic](https://docs.pydantic.dev/latest/) to model the data structure.

## Raw Data

The underlying data is structured in a way that allows for easy access. The raw data is stored in CSV files and is loaded into the library using the provided [models](data_model.md#models).

The CSV files are structured as follows:

* `yield_tables_meta.csv`: Contains metadata about the available yield tables.
    - `id`: The unique identifier of the yield table.
    - `name`: The name of the yield table.
    - `country_codes`: The ISO 3166-1 alpha-2 country codes of the countries the yield table is applicable to.
    - `type`: The type of the yield table (e.g. `dgz_100`).
    - `source`: The source of the yield table.
    - `link`: A link to the source of the yield table or the yield table itself.
    - `yield_value_step`: The step between the yield values.
    - `age_step`: The step between the ages.

* `yield_tables.csv`: Contains the yield tables.
    - `yt_id`: The unique identifier of the yield table.
    - `yt_name`: The name of the yield table.
    - `age`: The age in years.
    - `dominant_height`: The dominant height in m.
    - `middle_height`: The middle height in m.
    - `diameter`: The diameter in cm.
    - `taper`: The taper.
    - `trees_per_ha`: The number of trees per hectare.
    - `area`: The area in m2.
    - `volume_per_ha`: The volume per hectare in vfm.
    - `mean_volume_per_ha`: The mean volume per hectare vfm.
    - `total_volume_per_ha`: The total volume per hectare vfm.
    - `annual_volume_grow_per_ha`: The annual volume growth per hectare vfm.
    - `mean_total_growth_per_ha`: The mean total growth per hectare vfm.

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
