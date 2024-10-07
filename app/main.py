from fastapi import FastAPI
from contextlib import asynccontextmanager
from tortoise import Tortoise
from core.config import settings
from routers import breed_router, auth_router, permission_router, user_router, kitten_router, rating_router
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    await Tortoise.init(
        db_url=settings.DATABASE_URL,
        modules={"models": settings.MODELS}
    )
    await Tortoise.generate_schemas()
    yield
    await Tortoise.close_connections()


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router.router, tags=["auth"])
app.include_router(breed_router.router, tags=["breed"])
app.include_router(kitten_router.router, tags=["kitten"])
app.include_router(rating_router.router, tags=["rating"])
app.include_router(user_router.router, tags=["user"])
app.include_router(permission_router.router, tags=["permission"])


@app.get("/")
async def read_root():
    return {"message": "Hello, World from FastAPI with Tortoise ORM!"}
