from pydantic import ValidationError
import pytest

from openyieldtables.models import (
    YieldClass,
    YieldClassRow,
    YieldTable,
    YieldTableData,
    YieldTableMeta,
)
from openyieldtables.models.yieldtable import TreeType


def test_yield_table_meta_valid():
    # Test correct instantiation with valid data
    data = {
        "id": 1,
        "title": "yield_table_name",
        "country_codes": ["AT", "DE"],
        "type": "dgz_100",
        "source": "source",
        "link": "https://example.com",
        "yield_class_step": 1,
        "age_step": 10,
        "tree_type": TreeType.coniferous,
        "available_columns": [
            "id",
            "name",
            "yield_class",
            "age",
        ],
    }
    model = YieldTableMeta(**data)
    assert model.id == 1
    assert model.title == "yield_table_name"
    assert model.country_codes == ["AT", "DE"]
    assert model.yield_class_step == 1.0


def test_yield_table_meta_invalid():
    # Test instantiation with invalid data (should raise ValidationError)
    invalid_data = {
        "id": "not an int",  # Invalid type for 'id'
        "title": "yield_table_name",
        "country_codes": "AT",  # Invalid type for 'country_codes'
        "type": "dgz_100",
        "source": "source",
        "link": "https://example.com",
        "yield_class_step": 1,
        "age_step": 10,
        "tree_type": TreeType.coniferous,
        "available_columns": [],
    }
    with pytest.raises(ValidationError):
        YieldTableMeta(**invalid_data)

    invalid_data = {
        "id": 1,
        "title": "yield_table_name",
        "country_codes": ["AT"],
        "type": "dgz_100",
        "source": "source",
        "link": "https://example.com",
        "yield_class_step": 1,
        "age_step": 10,
        "tree_type": "invalid_tree_type",  # Invalid value for 'tree_type
        "available_columns": [],
    }
    with pytest.raises(ValidationError):
        YieldTableMeta(**invalid_data)


def test_yield_table_meta_defaults():
    # Test default values and behaviors
    data = {
        "id": 1,
        "title": "yield_table_name",
        "country_codes": ["AT"],
        "source": "source",
        "tree_type": TreeType.coniferous,
        "available_columns": [
            "id",
            "name",
            "yield_class",
            "age",
        ],
    }
    model = YieldTableMeta(**data)
    assert model.type is None
    assert model.link is None
    assert model.yield_class_step is None
    assert model.age_step is None


def test_yield_table_valid_data():
    # Test correct instantiation with valid data
    row = YieldClassRow(
        age=30,
        dominant_height=12.5,
        average_height=10.0,
        dbh=0.3,
        taper=0.1,
    )

    # Create a valid instance of YieldClass
    yield_class = YieldClass(yield_class=15, rows=[row])

    # Create a valid instance of YieldTableData
    data = YieldTableData(yield_classes=[yield_class])

    yield_table = YieldTable(
        id=1,
        title="yield_table_name",
        country_codes=["AT", "DE"],
        source="source",
        tree_type=TreeType.coniferous,
        available_columns=[
            "id",
            "name",
            "yield_class",
            "age",
        ],
        data=data,
    )

    # Assert that the data is correctly set in the YieldTable instance
    assert yield_table.id == 1
    assert yield_table.title == "yield_table_name"
    assert yield_table.data.yield_classes[0].yield_class == 15
    assert yield_table.data.yield_classes[0].rows[0].age == 30
    assert yield_table.data.yield_classes[0].rows[0].taper == 0.1


def test_yield_table_invalid_data():
    # Attempt to create a YieldTable with invalid data
    with pytest.raises(ValueError):
        YieldTable(
            id="invalid_id",  # Invalid type # type: ignore
            title="Sample Yield Table",
            country_codes=["US", "CA"],
            source="Some source",
            available_columns=["age", "dominant_height"],
            data=None,  # Empty data
        )
