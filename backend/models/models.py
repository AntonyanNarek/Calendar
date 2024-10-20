from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Date, Boolean

metadata = MetaData()

# Таблица person
person = Table(
    "person",
    metadata,
    Column("person_id", Integer, primary_key=True),
    Column("person_name", String(16), nullable=False),
    Column("tag_id", Integer, nullable=False),
    Column("premium", Boolean, nullable=False),
    Column("email", String(50), nullable=False),
    Column("status", String(50), nullable=False),
    Column("about", String(200), nullable=False),
    Column("phone", String(12), nullable=False),
    Column("theme", String(16), nullable=False),
    Column("password", String(50), nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
)

# Таблица room
room = Table(
    "room",
    metadata,
    Column("room_id", Integer, primary_key=True),
    Column("room_name", String(15), nullable=False),
    Column("link", String(50), nullable=False),
    Column("outdated", Date, nullable=False),
    Column("person_id", Integer, ForeignKey("person.person_id"), nullable=False),
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
    Column("person_id", Integer, ForeignKey("person.person_id"), nullable=False),
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
    Column("person_id", Integer, ForeignKey("person.person_id"), nullable=False),
    Column("day_id", Integer, ForeignKey("day.day_id"), nullable=False),
    Column("is_busy", Boolean, nullable=False),
)

# Таблица person_room
person_room = Table(
    "person_room",
    metadata,
    Column("person_room_id", Integer, primary_key=True),
    Column("person_id", Integer, ForeignKey("person.person_id"), nullable=False),
    Column("room_id", Integer, ForeignKey("room.room_id"), nullable=False),
    Column("color", String(50), nullable=False),
)