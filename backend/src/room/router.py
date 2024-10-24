from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from room.models import room
from room.schemas import RoomCreate

from auth.base_config import Person, current_user

router = APIRouter(
    prefix="/rooms",
    tags=["Room"]
)


def convert_rows_to_dicts(rows):
    rooms_list = []
    for row in rows:
        room_dict = {
            "room_id": row.room_id,
            "room_name": row.room_name,
            "link": row.link,
            "outdated": row.outdated,
            "person_id": row.person_id
        }
        rooms_list.append(room_dict)
    return rooms_list


@router.get("/rooms")
async def get_rooms(session: AsyncSession = Depends(get_async_session),
                    person: Person = Depends(current_user)):
    try:
        query = select(room)
        result = await session.execute(query)
        rooms = result.all()

        return convert_rows_to_dicts(rooms)
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
    })


@router.get("/specific_rooms")
async def get_specific_rooms(room_name: str, session: AsyncSession = Depends(get_async_session),
                             person: Person = Depends(current_user)):
    try:
        query = select(room).where(room.c.room_name.ilike(f"%{room_name}%"))
        result = await session.execute(query)
        rooms = result.all()

        return {
            "status": "success",
            "data": convert_rows_to_dicts(rooms),
            "details": f"Комнаты с названием {room_name}"
        }

    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/add_room")
async def add_specific_operations(new_operation: RoomCreate, session: AsyncSession = Depends(get_async_session),
                                  person: Person = Depends(current_user)):
    try:
        stmt = insert(room).values(**new_operation.dict())
        await session.execute(stmt)
        await session.commit()
        return {
                "status": "success",
                "data": None,
                "details": "Комната создана"
            }
    except Exception:
        raise HTTPException(status_code=400, detail={
            "status": "error",
            "data": None,
            "details": None
        })