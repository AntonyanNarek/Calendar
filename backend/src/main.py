from fastapi_users import FastAPIUsers

from fastapi import FastAPI, Depends
from redis import asyncio as aioredis
from auth.base_config import Person, current_user
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from auth.manager import get_user_manager
from fastapi.middleware.cors import CORSMiddleware
from auth.base_config import auth_backend, fastapi_users
from auth.schemas import PersonRead, PersonCreate
from room.router import router as router_room

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

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")