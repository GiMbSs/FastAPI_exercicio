from typing import Annotated
from datetime import datetime, timezone
from uuid import UUID, uuid4
from beanie import Document, Indexed, Link
from pydantic import Field
from .user_model import User

class Task(Document):
    task_id: UUID = Field(default_factory=uuid4, unique=True)
    status: bool = False
    title: Annotated[str, Indexed()]
    description: Annotated[str, Indexed()]
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    owner: Link[User]