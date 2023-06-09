from dagster import (
    define_asset_job,
    AssetSelection,
    load_assets_from_modules,
)

# Make sure all files with assets are imported:
from Giveways.assets import stores, deals

all_assets = load_assets_from_modules([stores, deals])

# Define jobs:

all_job = define_asset_job(
    description="All assets included, for UI visibility",
    name="AllAssets",
    selection=AssetSelection.all(),
)

def_job = define_asset_job(
    name="def_job_hourly",
    selection=AssetSelection.groups("default"),
    description="Defualt job runs hourly (could be used as a placeholder)",
)

stores_job = define_asset_job(
    name="stores_job",
    selection=AssetSelection.groups("stores"),
    description="Gets all stores data from cheapshark.com API",
)

deals_job = define_asset_job(
    name="deals_job",
    selection=AssetSelection.groups("deals"),
    description="Gets all deals from cheapshark.com API",
)

# Add job to list below:

jobs_list = [all_job, def_job, stores_job, deals_job]
