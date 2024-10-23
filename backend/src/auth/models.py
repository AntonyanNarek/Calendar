from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Date, Boolean
from database import Base

metadata = MetaData()

# Таблица person
person = Table(
    "person",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("person_name", String(16), nullable=False),
    Column("tag_id", Integer, nullable=False),
    Column("premium", Boolean, nullable=False),
    Column("email", String(50), nullable=False),
    Column("status", String(50), nullable=True),
    Column("about", String(200), nullable=True),
    Column("phone", String(12), nullable=False),
    Column("theme", String(16), nullable=True),
    Column("hashed_password", String(1024), nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    extend_existing=True
)


class Person(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'person'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    person_name = Column(String(length=16), nullable=False)
    tag_id = Column(Integer, nullable=False)
    premium = Column(Boolean, nullable=False)
    status = Column(String(length=50), nullable=True)
    about = Column(String(length=200), nullable=True)
    phone = Column(String(length=12), nullable=False)
    theme = Column(String(length=16), nullable=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    email = Column(String(length=50), nullable=False)
    hashed_password: str = Column(String(length=1024), nullable=False)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
    # role_id = Column(Integer, ForeignKey(role.c.id))

""""" Возможно таблицы только те пишутся, с которыми будет взаимодействие в рамках запроса
# Таблица room
room = Table(
    "room",
    metadata,
    Column("room_id", Integer, primary_key=True),
    Column("room_name", String(15), nullable=False),
    Column("link", String(50), nullable=False),
    Column("outdated", Date, nullable=False),
    Column("id", Integer, ForeignKey("person.id"), nullable=False),
)

# Таблица event
event = Table(
    "event",
    metadata,
    Column("event_id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("date", Date, nullable=False),
    Column("chat_id", Integer, nullable=False),
    Column("room_id", Integer, ForeignKey("room.room_id"), nullable=False),
    Column("num_members", Integer, nullable=False),
    Column("id", Integer, ForeignKey("person.id"), nullable=False),
)

# Таблица day
day = Table(
    "day",
    metadata,
    Column("day_id", Integer, primary_key=True),
    Column("date", Date, nullable=False),
    Column("room_id", Integer, ForeignKey("room.room_id"), nullable=False),
    Column("event_id", Integer, ForeignKey("event.event_id"), nullable=False),
    Column("comment", String(20), nullable=False),
)

# Таблица person_day
person_day = Table(
    "person_day",
    metadata,
    Column("person_day_id", Integer, primary_key=True),
    Column("comment", String(50), nullable=False),
    Column("id", Integer, ForeignKey("person.id"), nullable=False),
    Column("day_id", Integer, ForeignKey("day.day_id"), nullable=False),
    Column("is_busy", Boolean, nullable=False),
)

# Таблица person_room
person_room = Table(
    "person_room",
    metadata,
    Column("person_room_id", Integer, primary_key=True),
    Column("id", Integer, ForeignKey("person.id"), nullable=False),
    Column("room_id", Integer, ForeignKey("room.room_id"), nullable=False),
    Column("color", String(50), nullable=False),
)

"""""