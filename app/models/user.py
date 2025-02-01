from sqlalchemy import Table, Column, Integer, String
from ..database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), unique=True),
    Column("email", String(50), unique=True),
    Column("hashed_password", String(100)),
)
