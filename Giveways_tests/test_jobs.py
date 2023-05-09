from dagster import load_assets_from_modules, define_asset_job, AssetSelection
from . import test_assets as a


all_assets = load_assets_from_modules([a])

test_job = define_asset_job(name="test_job", selection=AssetSelection.all())

# Add job to list below:
job_list = [test_job]
