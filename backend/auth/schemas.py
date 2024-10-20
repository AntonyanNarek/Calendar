import uuid
from typing import Optional

from fastapi_users import schemas


class PersonRead(schemas.BaseUser[int]):
    id: int
    person_name: str
    email: str
    phone: str
    tag_id: int
    premium: bool
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class PersonCreate(schemas.BaseUserCreate):
    person_name: str
    email: str
    phone: str
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False