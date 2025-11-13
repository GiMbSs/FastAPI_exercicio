from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager

from models.user_model import User
from models.task_model import Task
from api.router import router

@asynccontextmanager
async def lifespan(app: FastAPI):

    client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    database = client.todoapp

    await init_beanie(
        database=database,
        document_models=[
            User,
            Task,
        ]
    )

    yield

    client.close()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f'{settings.API_V1_STR}/openapi.json',
    lifespan=lifespan
)

app.include_router(
    router,
    prefix=settings.API_V1_STR
)

