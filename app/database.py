import databases
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from .config import settings

database = databases.Database(settings.DATABASE_URL)
metadata = MetaData()

engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}  # Only needed for SQLite
)

def get_database() -> databases.Database:
    return database
