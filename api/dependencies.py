from openyieldtables.classes.data_management import DataFrameManager

# Create a DataFrameManager instance
df_manager = DataFrameManager()


async def get_yield_tables_data_dep():
    return await df_manager.get_yield_tables_data()


async def get_yield_tables_meta_dep():
    return await df_manager.get_yield_tables_meta()
