# Data Model

The `openyieldtables` library uses [pydantic](https://docs.pydantic.dev/latest/) to model the data structure.

## Raw Data

The underlying data is structured in a way that allows for easy access. The raw data is stored in CSV files and is loaded into the library using the provided [models](data_model.md#models).

The CSV files are structured as follows:

* `yield_tables_meta.csv`: Contains metadata about the available yield tables.
    - `id`: The unique identifier of the yield table.
    - `title`: The name/title of the yield table.
    - `country_codes`: The ISO 3166-1 alpha-2 country codes of the countries the yield table is applicable to.
    - `type`: The type of the yield table (e.g. `dgz_100`).
    - `source`: The source of the yield table.
    - `link`: A link to the source of the yield table or the yield table itself.
    - `yield_class_step`: The step between the yield classes.
    - `age_step`: The step between the ages.
    - `tree_type`: The tree type: `coniferous` or `deciduous`.

* `yield_tables.csv`: Contains the yield tables.
    - `id`: The unique identifier of the yield table.
    - `age`: The age in years.
    - `dominant_height`: The dominant height in m.
    - `average_height`: The average height in m.
    - `dbh`: The diameter at breast height in cm.
    - `taper`: The tree taper.
    - `trees_per_ha`: The number of trees per hectare.
    - `basal_area`: The basal area in m2.
    - `volume_per_ha`: The volume per hectare in vfm.
    - `average_annual_age_increment`: The average annual increment up to a certain age in volume per hectare vfm.
    - `total_growth_performance`: The total growth performance in volume per hectare vfm.
    - `current_annual_increment`: The current annual increment in volume per hectare vfm.
    - `mean_annual_increment`: The mean annual increment in volume per hectare vfm.

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
