from pathlib import Path

import numpy as np
import pandas as pd

from openyieldtables.models.yieldtable import TreeType

# Construct the path to the CSV files dynamically
script_location = Path(__file__).resolve().parents[1]
csv_path_meta = script_location / "data" / "yield_tables_meta.csv"
csv_path_yield_tables = script_location / "data" / "yield_tables.csv"


class DataFrameManager:
    def __init__(self):
        self.yield_tables_df = None
        self.yield_tables_meta_df = None

    async def load_yield_tables_data(self):
        """Loads the yield tables data from CSV file."""
        self.yield_tables_df = pd.read_csv(
            csv_path_yield_tables,
            delimiter=";",
        )
        # Preprocess the loaded data
        self.preprocess_yield_tables_data()

    async def load_yield_tables_meta(self):
        """Loads the yield tables meta data from CSV file."""
        self.yield_tables_meta_df = pd.read_csv(
            csv_path_meta,
            delimiter=";",
        )
        # Preprocess the loaded data
        self.preprocess_yield_tables_meta()

    def preprocess_yield_tables_data(self):
        """Preprocess the yield tables data."""
        if self.yield_tables_df is None:
            raise RuntimeError("Yield tables data is not loaded")
        # Replace missing data with None
        self.yield_tables_df.replace({np.nan: None}, inplace=True)

    def preprocess_yield_tables_meta(self):
        """Preprocess the yield tables meta data."""
        if self.yield_tables_meta_df is None:
            raise RuntimeError("Yield tables meta data is not loaded")
        # Handle missing string data by replacing it with empty strings
        self.yield_tables_meta_df.fillna(
            {
                "link": "",
                "type": "",
            },
            inplace=True,
        )
        # Replace other missing data with None
        self.yield_tables_meta_df.replace({np.nan: None}, inplace=True)
        # Apply transformations directly to DataFrame columns
        self.yield_tables_meta_df["country_codes"] = self.yield_tables_meta_df[
            "country_codes"
        ].apply(lambda x: x.split(",") if isinstance(x, str) else [])
        self.yield_tables_meta_df["tree_type"] = self.yield_tables_meta_df[
            "tree_type"
        ].apply(lambda x: TreeType(x) if isinstance(x, str) else None)
        # Find available columns for each yield table
        self.yield_tables_meta_df["available_columns"] = (
            self.yield_tables_meta_df["id"].apply(
                lambda x: self.find_available_columns("id", x)
            )
        )

    def find_available_columns(self, id_column: str, id_value: int) -> list:
        """Find columns in a DataFrame where at least one value is present
        for a specific ID."""
        if self.yield_tables_df is None:
            raise RuntimeError("Yield tables data is not loaded")
        filtered_df = self.yield_tables_df[
            self.yield_tables_df[id_column] == id_value
        ]
        return [
            col
            for col in filtered_df.columns
            if not filtered_df[col].isnull().all()
        ]

    async def get_yield_tables_data(self):
        """Returns the yield tables data."""
        if self.yield_tables_df is None:
            raise RuntimeError("Yield tables data is not loaded")
        return self.yield_tables_df

    async def get_yield_tables_meta(self):
        """Returns the yield tables meta data."""
        if self.yield_tables_meta_df is None:
            raise RuntimeError("Yield tables meta data is not loaded")
        return self.yield_tables_meta_df
