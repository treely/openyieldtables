from pydantic import ValidationError
import pytest

from models import (
    YieldClass,
    YieldClassRow,
    YieldTable,
    YieldTableData,
    YieldTableMeta,
)


def test_yield_table_meta_valid():
    # Test correct instantiation with valid data
    data = {
        "id": 1,
        "name": "yield_table_name",
        "tree_species_id": 1000000,
        "name_short": "short_name",
        "country_codes": ["AT", "DE"],
        "type": "dgz_100",
        "assortment_table": 1,
        "weight": 420,
        "source": "source",
        "active": True,
        "yield_value_step": 1,
        "age_step": 10,
        "age_min": 10,
        "age_max": 250,
        "missing_columns": None,
        "available_columns": [
            "id",
            "name",
            "yield_value",
            "age",
        ],
    }
    model = YieldTableMeta(**data)
    assert model.id == 1
    assert model.name == "yield_table_name"
    assert model.country_codes == ["AT", "DE"]
    assert model.yield_value_step == 1.0
    assert model.missing_columns is None


def test_yield_table_meta_invalid():
    # Test instantiation with invalid data (should raise ValidationError)
    invalid_data = {
        "id": "not an int",  # Invalid type for 'id'
        "name": "yield_table_name",
        "tree_species_id": 1000000,
        "name_short": "short_name",
        "country_codes": "AT",  # Invalid type for 'country_codes'
        "type": "dgz_100",
        "assortment_table": 1,
        "weight": 420.8,  # Invalid type for 'weight'
        "source": "source",
        "active": True,
        "yield_value_step": 1,
        "age_step": 10,
        "age_min": 10,
        "age_max": 250,
        "missing_columns": None,
        "available_columns": [],
    }
    with pytest.raises(ValidationError):
        YieldTableMeta(**invalid_data)


def test_yield_table_meta_defaults():
    # Test default values and behaviors
    data = {
        "id": 1,
        "name": "yield_table_name",
        "country_codes": ["AT"],
        "source": "source",
        "available_columns": [
            "id",
            "name",
            "yield_value",
            "age",
        ],
    }
    model = YieldTableMeta(**data)
    assert model.tree_species_id is None
    assert model.active is None
    assert model.missing_columns is None


def test_yield_table_valid_data():
    # Test correct instantiation with valid data
    row = YieldClassRow(
        age=30,
        dominant_height=12.5,
        middle_height=10.0,
        diameter=0.3,
        taper=0.1,
    )

    # Create a valid instance of YieldClass
    yield_class = YieldClass(yield_value=15, rows=[row])

    # Create a valid instance of YieldTableData
    data = YieldTableData(yield_classes=[yield_class])

    yield_table = YieldTable(
        id=1,
        name="yield_table_name",
        country_codes=["AT", "DE"],
        source="source",
        available_columns=[
            "id",
            "name",
            "yield_value",
            "age",
        ],
        data=[data],
    )

    # Assert that the data is correctly set in the YieldTable instance
    assert yield_table.id == 1
    assert yield_table.name == "yield_table_name"
    assert yield_table.data[0].yield_classes[0].yield_value == 15
    assert yield_table.data[0].yield_classes[0].rows[0].age == 30
    assert yield_table.data[0].yield_classes[0].rows[0].taper == 0.1


def test_yield_table_invalid_data():
    # Attempt to create a YieldTable with invalid data
    with pytest.raises(ValueError):
        YieldTable(
            id="invalid_id",  # Invalid type
            name="Sample Yield Table",
            country_codes=["US", "CA"],
            source="Some source",
            available_columns=["age", "dominant_height"],
            data=[],  # Empty data
        )
