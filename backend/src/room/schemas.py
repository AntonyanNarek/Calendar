from datetime import datetime

from pydantic import BaseModel, Field, validator


class RoomCreate(BaseModel):
    room_id: int
    room_name: str = Field(max_length=15)
    link: str
    outdated: datetime
    person_id: int
