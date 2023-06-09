import datetime
import requests
import pandas as pd
from dagster import asset, multi_asset, AssetOut, Output, AssetIn
from sqlalchemy import types
from .config.database_connection import engine_create

# Place your assests here:


@asset(group_name="stores", description="Gets all stores from cheapshark.com API")
def store_data_get() -> str:
    url = "https://www.cheapshark.com/api/1.0/stores"
    data = requests.get(url)
    return data.text


@asset(group_name="stores", description="Converts stores data to pandas dataframe")
def store_data_to_df(store_data_get) -> pd.DataFrame:
    df = pd.read_json(store_data_get)
    return df


@asset(
    group_name="stores",
    description="Saves stores data to PostgreSQL database",
)
def store_data_to_sql(store_data_to_df) -> None:
    df = store_data_to_df
    with engine_create().connect() as conn:
        df.to_sql(
            con=conn,
            name="store_info",
            if_exists="replace",
            index=False,
            dtype={"images": types.JSON},
            chunksize=1000,
        )
