import datetime
import requests
import pandas as pd
from dagster import asset, multi_asset, AssetOut, Output
from .config.database_connection import conn


# Place your assests here:


@asset(group_name="deals", description="Gets all deals from cheapshark.com API")
def get_data_deals():
    url = "https://www.cheapshark.com/api/1.0/deals?pageNumber="
    page = 1
    all_data = []
    while True:
        request = requests.get(f"{url}{page}&pageSize=60")
        if request.status_code != 200:
            break
        data = request.json()
        all_data.extend(data)
        page += 1
    return all_data


@asset(group_name="deals", description="Converts deals data to pandas dataframe")
def pr_data(get_data_deals):
    df = pd.DataFrame(get_data_deals)
    return Output(
        value=df,
        metadata={
            "Number of rows": len(df.index),
            "Number of columns": len(df.columns),
        },
    )


@asset(group_name="deals", description="Transforms dataframe")
def data_transform(pr_data):
    pr_data["releaseDate"] = pd.to_datetime(pr_data["releaseDate"], unit="s")
    pr_data["lastChange"] = pd.to_datetime(pr_data["lastChange"], unit="s")
    return pr_data


@asset(group_name="deals", description="Saves data to PostgreSQL database")
def data_to_sql(data_transform):
    data_transform.to_sql(
        con=conn, name="deals", if_exists="replace", index=False, chunksize=1000
    )
