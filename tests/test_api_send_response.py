from fastapi.testclient import TestClient
import pytest

from api.main import app

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # https://fastapi.tiangolo.com/advanced/testing-events/
    with client:
        yield


def test_api_send_response_as_html():
    # Read yield table data as HTML
    response = client.get(
        "/v1/yield-tables/1", headers={"accept": "text/html"}
    )

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_api_send_response_as_json():
    # Read yield table data as JSON
    response = client.get(
        "/v1/yield-tables/1", headers={"accept": "application/json"}
    )

    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
