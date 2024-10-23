from datetime import datetime

from pydantic import BaseModel


class RoomCreate(BaseModel):
    room_id: int
    room_name: str
    link: str
    outdated: datetime
    person_id: int