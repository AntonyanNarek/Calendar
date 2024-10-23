from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Date, Boolean

from auth.models import person
from database import Base

metadata = MetaData()


# Таблица room
room = Table(
    "room",
    metadata,
    Column("room_id", Integer, primary_key=True),
    Column("room_name", String(15), nullable=False),
    Column("link", String(50), nullable=False),
    Column("outdated", Date, nullable=False),
    Column("person_id", Integer, ForeignKey(person.c.id), nullable=False),
)