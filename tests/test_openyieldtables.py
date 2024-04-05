import pytest

from openyieldtables.yieldtables import (
    get_yield_table_data,
    get_yield_tables_meta,
)


def test_get_yield_tables_meta():
    yield_tables_meta = get_yield_tables_meta()
    assert len(yield_tables_meta) == 78

    assert yield_tables_meta[0].model_dump() == {
        "id": 1,
        "name": "Fichte_Hochgebirge",
        "tree_species_id": 1000000,
        "name_short": "Fi-HG",
        "country_codes": ["AT", "DE"],
        "type": "dgz_100",
        "assortment_table": None,
        "weight": 420,
        "source": "Marschall",
        "active": True,
        "yield_value_step": 1.0,
        "age_step": 10,
        "age_min": 10,
        "age_max": 250,
        "missing_columns": [],
        "available_columns": [
            "yt_id",
            "yt_name",
            "yield_value",
            "age",
            "dominant_height",
            "middle_height",
            "diameter",
            "taper",
            "trees_per_ha",
            "area",
            "volume_per_ha",
            "mean_volume_growth_per_ha",
            "total_volume_per_ha",
            "annual_volume_grow_per_ha",
            "mean_total_growth_per_ha",
        ],
    }
    assert yield_tables_meta[77].model_dump() == {
        "id": 93,
        "name": "Ki-SüdTirol  ",
        "tree_species_id": 10001,
        "name_short": "Ki-SüdTirol  ",
        "country_codes": ["AT", "DE"],
        "type": "dgz_150",
        "assortment_table": None,
        "weight": 460,
        "source": "ET-digital.xls",
        "active": True,
        "yield_value_step": 1.0,
        "age_step": 10,
        "age_min": 10,
        "age_max": 250,
        "missing_columns": [],
        "available_columns": [
            "yt_id",
            "yt_name",
            "yield_value",
            "age",
            "dominant_height",
            "middle_height",
            "diameter",
            "taper",
            "trees_per_ha",
            "area",
            "volume_per_ha",
            "mean_volume_growth_per_ha",
            "total_volume_per_ha",
            "annual_volume_grow_per_ha",
            "mean_total_growth_per_ha",
        ],
    }


def test_get_yield_table_data():
    yield_table_data = get_yield_table_data(1)
    assert yield_table_data.data[0].yield_classes[5].rows[0].model_dump() == {
        "age": 20,
        "dominant_height": 4.8,
        "middle_height": 4.3,
        "diameter": 6.7,
        "taper": 0.153,
        "trees_per_ha": 5288.0,
        "area": None,
        "volume_per_ha": 12.0,
        "mean_volume_growth_per_ha": 0.6,
        "total_volume_per_ha": 13.0,
        "annual_volume_grow_per_ha": None,
        "mean_total_growth_per_ha": 0.6,
    }

    yield_table_data = get_yield_table_data(93)
    assert yield_table_data.data[0].yield_classes[0].rows[0].model_dump() == {
        "age": 100,
        "dominant_height": 8.1,
        "middle_height": 7.2,
        "diameter": 12.5,
        "taper": 0.53,
        "trees_per_ha": 3358.0,
        "area": 41.5,
        "volume_per_ha": 159.0,
        "mean_volume_growth_per_ha": 1.59,
        "total_volume_per_ha": 178.0,
        "annual_volume_grow_per_ha": None,
        "mean_total_growth_per_ha": 1.8,
    }

    with pytest.raises(ValueError):
        get_yield_table_data(999)
