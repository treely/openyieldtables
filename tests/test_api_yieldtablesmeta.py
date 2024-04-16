from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_read_yield_tables_meta():
    response = client.get("/v1/yield-tables-meta")
    assert response.status_code == 200
    assert len(response.json()) == 67
    assert response.json()[0] == {
        "id": 1,
        "name": "Fichte_Hochgebirge",
        "country_codes": ["AT", "DE"],
        "type": "dgz_100",
        "source": "Marschall",
        "link": "",
        "yield_value_step": 1.0,
        "age_step": 10,
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
    assert response.json()[27] == {
        "id": 93,
        "name": "Ki-SüdTirol  ",
        "country_codes": ["AT", "DE"],
        "type": "dgz_150",
        "source": "ET-digital.xls",
        "link": "",
        "yield_value_step": 1.0,
        "age_step": 10,
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


def test_read_yield_table_meta():
    response = client.get("/v1/yield-tables-meta/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Fichte_Hochgebirge",
        "country_codes": ["AT", "DE"],
        "type": "dgz_100",
        "source": "Marschall",
        "link": "",
        "yield_value_step": 1.0,
        "age_step": 10,
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
