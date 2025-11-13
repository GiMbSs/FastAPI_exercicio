from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.security import create_access_token, create_refresh_token
from schemas.auth_schema import TokenSchema
from schemas.user_schema import UserDetail
from models.user_model import User
from api.depedencies.user_deps import get_current_user

auth_router = APIRouter()

@auth_router.post('/login', summary='Cria Access Token e Refresh Token', response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email = data.username,
        password = data.password
    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='E-mail ou senha incorretos ou inexistentes'
        )
    return {
        "access_token": create_access_token(usuario.user_id),
        "refresh_token": create_refresh_token(usuario.user_id)
    }

@auth_router.post('/test-token', summary='Testando token', response_model=UserDetail)
async def test_token(user: User | None = Depends(get_current_user)):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token inválido ou usuário não encontrado')
    return user
