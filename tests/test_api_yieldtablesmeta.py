from fastapi.testclient import TestClient

from api.main import app
from openyieldtables.models.yieldtable import TreeType

client = TestClient(app, headers={"accept": "application/json"})


def test_read_yield_tables_meta():
    response = client.get("/v1/yield-tables-meta")
    assert response.status_code == 200
    assert len(response.json()) == 49
    assert response.json()[0] == {
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
    assert response.json()[27] == {
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


def test_read_yield_table_meta():
    response = client.get("/v1/yield-tables-meta/1")
    assert response.status_code == 200
    assert response.json() == {
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

    response = client.get("/v1/yield-tables-meta/999")
    assert response.status_code == 404
    assert response.json() == {
        "detail": {"message": "Yield table with ID 999 not found."}
    }

    response = client.get("/v1/yield-tables-meta/not_an_int")
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "int_parsing",
                "loc": ["path", "yield_table_id"],
                "msg": "Input should be a valid integer, unable to parse string as an integer",  # noqa: E501
                "input": "not_an_int",
                "url": "https://errors.pydantic.dev/2.6/v/int_parsing",
            }
        ]
    }
