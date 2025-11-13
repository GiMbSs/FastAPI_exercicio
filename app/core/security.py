import bcrypt
from typing import Union, Any
from datetime import datetime, timedelta, timezone
from jose import jwt
from core.config import settings

def get_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed_pass: str) -> bool:
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        password_bytes = password_bytes[:72]
    return bcrypt.checkpw(password_bytes, hashed_pass.encode('utf-8'))

def create_access_token(subject: Union[str, Any], expires_delta: timedelta | None = None) -> str:
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    payload = {"exp": expire, "sub": str(subject)}
    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)

def create_refresh_token(subject: Union[str, Any], expires_delta: timedelta | None = None) -> str:
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.REFRESH_TOKENS_EXPIRE_MINUTES))
    payload = {"exp": expire, "sub": str(subject)}
    return jwt.encode(payload, settings.JWT_REFRESH_SECRET_KEY, algorithm=settings.ALGORITHM)

    