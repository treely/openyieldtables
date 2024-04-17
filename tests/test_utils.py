from openyieldtables.utils import find_available_columns, parse_float


def test_find_available_columns():
    # Yield table with empty columns
    available_columns = find_available_columns(
        "src/openyieldtables/data/yield_tables.csv", "id", 7
    )
    assert available_columns == [
        "id",
        "yield_class",
        "age",
        "average_height",
        "dbh",
        "taper",
        "trees_per_ha",
        "basal_area",
        "volume_per_ha",
        "total_growth_performance",
        "current_annual_increment",
        "mean_annual_increment",
    ]

    # Yield table without empty columns
    available_columns = find_available_columns(
        "src/openyieldtables/data/yield_tables.csv", "id", 1
    )
    assert available_columns == [
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
    ]


def test_parse_float():
    assert parse_float("1,23") is None
    assert parse_float("1.23") == 1.23
    assert parse_float(None) is None
    assert parse_float("abc") is None
    assert parse_float("1,23,45") is None
    assert parse_float("1.23.45") is None
    assert parse_float("1.23abc") is None
    assert parse_float("1,23abc") is None
