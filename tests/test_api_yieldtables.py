from fastapi.testclient import TestClient

from api.main import app
from openyieldtables.models import YieldTable

client = TestClient(app)


def test_read_yield_table_data():
    response = client.get("/v1/yield-tables/1")
    assert response.status_code == 200

    yield_table = YieldTable(**response.json())
    row = yield_table.data[0].yield_classes[0].rows[0]

    assert row.age == 20
    assert row.dominant_height == 5.9
    assert row.middle_height == 5.3
    assert row.diameter == 11.5
    assert row.taper == 0.396
    assert row.trees_per_ha == 2585
    assert row.area == 26.8
    assert row.volume_per_ha == 54
    assert row.mean_volume_growth_per_ha == 2.7
    assert row.total_volume_per_ha == 63
    assert row.annual_volume_grow_per_ha is None
    assert row.mean_total_growth_per_ha == 3.2

    response = client.get("/v1/yield-tables/999")
    assert response.status_code == 404
    assert response.json() == {
        "detail": {"message": "Yield table with ID 999 not found."}
    }

    response = client.get("/v1/yield-tables/not_an_int")
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
