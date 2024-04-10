import csv
from typing import Dict, List, Optional, TypedDict, cast

from models import (
    YieldClass,
    YieldClassRow,
    YieldTable,
    YieldTableData,
    YieldTableMeta,
)

from .utils import find_available_columns, parse_float


class YieldTableMetaCSVRow(TypedDict, total=False):
    id: int
    name: str
    country_codes: List[str]
    type: Optional[str]
    source: str
    link: Optional[str]
    yield_value_step: Optional[float]
    age_step: Optional[int]
    available_columns: List[str]


def get_yield_tables_meta() -> List[YieldTableMeta]:
    """
    Reads the yield tables metadata from 'data/yield_tables_meta.csv' and
    returns a list of YieldTableMeta instances.

    The CSV file is expected to be in a specific format, with columns for
    tree_species_id, assortment table, weight, age_step, age_min, age_max, etc.

    Returns:
        List[YieldTableMeta]: A list of YieldTableMeta instances, one for each
        row in the CSV file.
    """

    yield_table_meta_list = []

    with open(
        "data/yield_tables_meta.csv",
        mode="r",
        encoding="utf-8",
    ) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")

        for row in reader:
            csv_row = cast(
                YieldTableMetaCSVRow,
                {
                    "id": int(row.get("id", 0)),
                    "name": row.get("name", ""),
                    "country_codes": (
                        row.get("country_codes", "").split(",")
                        if row.get("country_codes")
                        else []
                    ),
                    "type": row.get("type"),
                    "source": row.get("source", ""),
                    "link": row.get("link", ""),
                    "yield_value_step": (
                        float(row["yield_value_step"])
                        if row.get("yield_value_step")
                        else None
                    ),
                    "age_step": (
                        int(row["age_step"]) if row.get("age_step") else None
                    ),
                    "available_columns": find_available_columns(
                        "data/yield_tables.csv", "yt_id", int(row["id"])
                    ),
                },
            )

            yield_table_meta = YieldTableMeta(**csv_row)
            yield_table_meta_list.append(yield_table_meta)

    return yield_table_meta_list


def get_yield_table_meta(yt_id: int) -> YieldTableMeta:
    """
    Reads the yield table metadata for a specific yield table ID from
    'data/yield_tables_meta.csv' and returns a YieldTableMeta instance.

    The CSV file is expected to be in a specific format, with columns for
    tree_species_id, assortment table, weight, age_step, age_min, age_max, etc.

    Args:
        yt_id (int): The ID of the yield table to get the metadata for.

    Raises:
        ValueError: If the yield table with the specified ID is not found.

    Returns:
        YieldTableMeta: A YieldTableMeta instance for the specified yield table
        ID.
    """

    yield_table_meta_list = get_yield_tables_meta()

    for yield_table_meta in yield_table_meta_list:
        if yield_table_meta.id == yt_id:
            return yield_table_meta

    raise ValueError(f"Yield table with ID {yt_id} not found.")


def get_yield_table_data(yt_id: int) -> YieldTable:
    """
    Reads the yield table data for a specific yield table ID from
    'data/yield_tables.csv' and returns a YieldTable instance.

    The CSV file is expected to be in a specific format, with columns for
    yt_id, yt_name, yield_value, age, dominant_height, middle_height, etc.

    Args:
        yt_id (int): The ID of the yield table to get the data for.

    Returns:
        YieldTable: A YieldTable instance for the specified yield table ID.
    """

    # Get the meta data
    yield_table_meta = get_yield_table_meta(yt_id)

    with open(
        "data/yield_tables.csv",
        mode="r",
        encoding="utf-8",
    ) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        filtered_data = [row for row in reader if int(row["yt_id"]) == yt_id]

    # Organizing data into YieldClasses
    yield_classes_dict: Dict[int, List[YieldClassRow]] = {}
    for row in filtered_data:
        yield_value = int(row["yield_value"])
        if yield_value not in yield_classes_dict:
            yield_classes_dict[yield_value] = []
        yield_classes_dict[yield_value].append(
            YieldClassRow(
                age=int(row["age"]),
                dominant_height=parse_float(row.get("dominant_height")),
                middle_height=parse_float(row.get("middle_height")),
                diameter=parse_float(row.get("diameter")),
                taper=parse_float(row.get("taper")),
                trees_per_ha=parse_float(row.get("trees_per_ha")),
                area=parse_float(row.get("area")),
                volume_per_ha=parse_float(row.get("volume_per_ha")),
                mean_volume_growth_per_ha=parse_float(
                    row.get("mean_volume_growth_per_ha")
                ),
                total_volume_per_ha=parse_float(
                    row.get("total_volume_per_ha")
                ),
                annual_volume_grow_per_ha=parse_float(
                    row.get("annual_volume_grow_per_ha")
                ),
                mean_total_growth_per_ha=parse_float(
                    row.get("mean_total_growth_per_ha")
                ),
            )
        )

    yield_classes = [
        YieldClass(yield_value=yv, rows=rows)
        for yv, rows in yield_classes_dict.items()
    ]

    return YieldTable(
        **yield_table_meta.model_dump(),
        data=[YieldTableData(yield_classes=yield_classes)],
    )
