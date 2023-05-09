from dagster import Definitions, load_assets_from_modules
from . import test_assets as a, test_jobs as j

all_assets = load_assets_from_modules([a])

defs = Definitions(assets=all_assets, jobs=j.job_list)
