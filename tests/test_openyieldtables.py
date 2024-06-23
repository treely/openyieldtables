import pytest

from openyieldtables.models.yieldtable import TreeType
from openyieldtables.yieldtables import get_yield_table, get_yield_tables_meta


def test_get_yield_tables_meta():
    yield_tables_meta = get_yield_tables_meta()

    assert yield_tables_meta[0].model_dump() == {
        "id": 1,
        "title": "Fichte Hochgebirge",
        "country_codes": ["AT", "DE"],
        "type": "dgz_100",
        "source": "1975, Julius Marschall: Hilfstafeln für die Forsteinrichtung, Neunte Auflage, Österreichischer Agrarverlag",  # noqa E501
        "link": "https://www.avbuch-shop.at/landwirtschaft/lehrbuecher/1347/hilfstafeln-fuer-die-forsteinrichtung",  # noqa E501
        "yield_class_step": 1.0,
        "age_step": 10,
        "tree_type": TreeType.coniferous,
        "available_columns": [
            "id",
            "yield_class",
            "age",
            "dominant_height",
            "average_height",
            "dbh",
            "taper",
            "trees_per_ha",
            "basal_area",
            "volume_per_ha",
            "average_annual_age_increment",
            "total_growth_performance",
            "current_annual_increment",
            "mean_annual_increment",
        ],
    }
    assert yield_tables_meta[27].model_dump() == {
        "id": 93,
        "title": "Tirol Kiefer Suedtirol",
        "country_codes": ["AT", "DE"],
        "type": "dgz_150",
        "source": "Ertragstafeln für Tirol, Amt der Tiroler Landesregierung",
        "link": "https://www.tirol.gv.at/umwelt/wald/waldwirtschaft/ertragstafeln-in-tirol/",  # noqa E501
        "yield_class_step": 1.0,
        "age_step": 10,
        "tree_type": TreeType.coniferous,
        "available_columns": [
            "id",
            "yield_class",
            "age",
            "dominant_height",
            "average_height",
            "dbh",
            "taper",
            "trees_per_ha",
            "basal_area",
            "volume_per_ha",
            "average_annual_age_increment",
            "total_growth_performance",
            "current_annual_increment",
            "mean_annual_increment",
        ],
    }


def test_get_yield_table():
    yield_table_data = get_yield_table(1)
    assert yield_table_data.data.yield_classes[5].rows[0].model_dump() == {
        "age": 20,
        "dominant_height": 4.8,
        "average_height": 4.3,
        "dbh": 6.7,
        "taper": 0.153,
        "trees_per_ha": 5288.0,
        "basal_area": None,
        "volume_per_ha": 12.0,
        "average_annual_age_increment": 0.6,
        "total_growth_performance": 13.0,
        "current_annual_increment": None,
        "mean_annual_increment": 0.6,
    }

    yield_table_data = get_yield_table(93)
    assert yield_table_data.data.yield_classes[0].rows[0].model_dump() == {
        "age": 100,
        "dominant_height": 8.1,
        "average_height": 7.2,
        "dbh": 12.5,
        "taper": 0.53,
        "trees_per_ha": 3358.0,
        "basal_area": 41.5,
        "volume_per_ha": 159.0,
        "average_annual_age_increment": 1.59,
        "total_growth_performance": 178.0,
        "current_annual_increment": None,
        "mean_annual_increment": 1.8,
    }

    yield_table_data = get_yield_table(144)
    assert yield_table_data.data.yield_classes[0].rows[0].model_dump() == {
        "age": 10,
        "dominant_height": None,
        "average_height": None,
        "dbh": None,
        "taper": None,
        "trees_per_ha": None,
        "basal_area": None,
        "volume_per_ha": 0,
        "average_annual_age_increment": None,
        "total_growth_performance": None,
        "current_annual_increment": None,
        "mean_annual_increment": None,
    }

    # yield_class is a float
    yield_table_data = get_yield_table(102)
    assert yield_table_data.data.yield_classes[0].yield_class == 0.4
    assert yield_table_data.data.yield_classes[8].yield_class == 3

    # Yield table ID is not found
    with pytest.raises(ValueError):
        get_yield_table(999)
