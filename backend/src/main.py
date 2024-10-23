from fastapi_users import FastAPIUsers

from fastapi import FastAPI, Depends

from auth.base_config import Person, current_user
from auth.manager import get_user_manager
from auth.base_config import auth_backend, fastapi_users
from auth.schemas import PersonRead, PersonCreate
from room.router import router as router_room #потом добавить

app = FastAPI(
    title="Calenfi"
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


@app.get("/protected-route")
def protected_route(person: Person = Depends(current_user)):
    return f"Hello, {person.person_name}"


@app.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"
    

app.include_router(router_room) #операция с роутом