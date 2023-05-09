from dagster import ScheduleDefinition, DefaultScheduleStatus, Definitions
from . import jobs as j


# Define schedules:

def_schedule = ScheduleDefinition(job=j.def_job, cron_schedule="33 0/3 * * *")

stores_schedule = ScheduleDefinition(
    job=j.stores_job,
    cron_schedule="0 0/2 * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)

deals_schedule = ScheduleDefinition(
    job=j.deals_job,
    cron_schedule="5 0/2 * * *",
    default_status=DefaultScheduleStatus.RUNNING,
)

# Add schedule to list below:

all_schedules = [def_schedule, deals_schedule, stores_schedule]

# Dagster project definitions:
defs = Definitions(assets=j.all_assets, schedules=all_schedules, jobs=j.jobs_list)
