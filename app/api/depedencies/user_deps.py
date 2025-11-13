from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from models.user_model import User
from jose import JWTError, jwt
from core.config import settings
from schemas.auth_schema import TokenPayLoad
from datetime import datetime, timezone
from pydantic import ValidationError
from services.user_service import UserService
from uuid import UUID

oauth_reusable = OAuth2PasswordBearer(
    tokenUrl=f'{settings.API_V1_STR}/auth/login',
    scheme_name='JWT'
)

async def get_current_user(token: str = Depends(oauth_reusable)) -> User:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayLoad(**payload)
        if datetime.fromtimestamp(token_data.exp, tz=timezone.utc) < datetime.now(timezone.utc):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='Token foi expirado',
                headers={'WWW-Authenticate': 'Bearer'}
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Erro na validação do token',
            headers={'WWW-Authenticate': 'Bearer'}
        )
    
    try:
        user_id = UUID(str(token_data.sub))
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Token inválido',
            headers={'WWW-Authenticate': 'Bearer'}
        ) from exc

    user = await UserService.get_user_by_id(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não foi possivel encontar o usuário',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return user
