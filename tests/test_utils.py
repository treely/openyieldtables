from openyieldtables.utils import find_available_columns, parse_float


def test_find_available_columns():
    # Yield table with empty columns
    empty_columns = find_available_columns("data/yield_tables.csv", "yt_id", 7)
    assert empty_columns == [
        "yt_id",
        "yt_name",
        "yield_value",
        "age",
        "middle_height",
        "diameter",
        "taper",
        "trees_per_ha",
        "area",
        "volume_per_ha",
        "total_volume_per_ha",
        "annual_volume_grow_per_ha",
        "mean_total_growth_per_ha",
    ]

    # Yield table without empty columns
    empty_columns = find_available_columns("data/yield_tables.csv", "yt_id", 1)
    assert empty_columns == [
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
