from sqlalchemy import engine


# Database connection

USERNAME = "dagster"
PASSWORD = "dagster"
DRIVER = "postgresql"
DATABASE_HOST = "postgres"
PORT = "5432"
DATABASE_NAME = "giveways"

conn = engine.create_engine(
    f"{DRIVER}://{USERNAME}:{PASSWORD}@{DATABASE_HOST}:{PORT}/{DATABASE_NAME}"
)
