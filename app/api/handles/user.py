from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserAuth, UserDetail
from services.user_service import UserService
import pymongo

user_router = APIRouter()

@user_router.post('/add', summary='Adiciona usuário', response_model=UserDetail)
async def add_user(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Usuáio ou email já existente'
        )