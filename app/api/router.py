from fastapi import APIRouter
from .handles import user
from api.auth.jwt import auth_router
from api.handles.task import task_router

router = APIRouter()

router.include_router(
    user.user_router,
    prefix='/users',
    tags=['users']
)

router.include_router(
    auth_router,
    prefix='/auth',
    tags=['auth']
)

router.include_router(
    task_router,
    prefix='/task',
    tags=['task']
)
