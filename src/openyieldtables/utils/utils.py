from pathlib import Path
from typing import List, Optional, Union

import pandas as pd


def find_available_columns(
    csv_path: Union[str, Path], id_column: str, id_value: int
) -> List[str]:
    """
    Find columns in a CSV file where at least one value is present for a
    specific ID.

    Args:
        csv_path (str): Path to the CSV file id_column (str): Name of the
        column containing the ID id_value (int): Value of the ID to filter the
        rows

    Returns:
        List[str]: A list of column names where at least one value is present
        for the given ID
    """

    # Read the CSV file
    df = pd.read_csv(csv_path, delimiter=";")

    # Filter rows based on the ID
    filtered_df = df[df[id_column] == id_value]

    # Find columns where not all values are NaN or None
    available_columns = [
        col
        for col in filtered_df.columns
        if not filtered_df[col].isnull().all()
    ]

    return available_columns


def parse_float(value: Optional[str]) -> Optional[float]:
    """
    Parse a string to float, handling None values.

    Args:
        value (Optional[str]): The string to parse. Can be None.

    Returns:
        Optional[float]: The parsed float value or None if parsing fails
    """

    if value is None:
        return None
    try:
        return float(value)
    except ValueError:
        return None
