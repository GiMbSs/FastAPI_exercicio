from beanie import Document, Indexed
from uuid import UUID, uuid4
from pydantic import Field, EmailStr
from datetime import datetime
from typing import Optional, Annotated

class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: Annotated[str, Indexed(unique=True)]
    email: Annotated[EmailStr, Indexed(unique=True)]
    hash_password: str
    firist_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = None

    def __repr__(self) -> str:
        return f'User {self.email}'
    
    def __str__(self) -> str:
        return self.email
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def create(self) -> datetime:
        return self.id.generation_time
    
    @classmethod
    async def by_email(cls, email: str) -> 'User':
        return await cls.find_one(cls.email == email)
        
