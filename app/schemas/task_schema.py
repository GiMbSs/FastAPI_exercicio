from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime

class TaskCreate(BaseModel):
    title: str = Field(..., title='Título da tarefa', min_length=3, max_length=50)
    description: str = Field(..., title='Descrição da tarefa', min_length=3, max_length=255)
    status: Optional[bool] = Field(False, title='Status da tarefa')

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, title='Título da tarefa')
    description: Optional[str] = Field(None, title='Descrição da tarefa')
    status: Optional[bool] = Field(None, title='Status da tarefa')

class UserOwner(BaseModel):
    user_id: UUID
    username: str
    email: str

class TaskDetail(BaseModel):
    task_id: UUID
    title: str
    description: str
    status: bool
    created_at: datetime
    updated_at: datetime
    owner: UserOwner
