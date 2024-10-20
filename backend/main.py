from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from fastapi_users import fastapi_users, FastAPIUsers
from pydantic import BaseModel, Field

from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder

from fastapi.responses import JSONResponse

from auth.database import Person
from auth.manager import get_user_manager
from auth.auth import auth_backend

from auth.schemas import PersonRead, PersonCreate

app = FastAPI(
    title="Trading App"
)

fastapi_users = FastAPIUsers[Person, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(PersonRead, PersonCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

@app.get("/protected-route")
def protected_route(person: Person = Depends(current_user)):
    return f"Hello, {person.person_name}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"