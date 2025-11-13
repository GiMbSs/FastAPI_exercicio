from models.user_model import User
from models.task_model import Task
from typing import List
from schemas.task_schema import TaskCreate, TaskDetail, TaskUpdate
from datetime import datetime, timezone

from uuid import UUID

class TaskService:
    @staticmethod
    async def list_tasks(user: User) -> List[TaskDetail]:
        tasks = await Task.find(Task.owner.id == user.id).to_list()
        result = []
        for task in tasks:
            task_detail = TaskDetail(
                task_id=task.task_id,
                title=task.title,
                description=task.description,
                status=task.status,
                created_at=task.created_at,
                updated_at=task.updated_at,
                owner={
                    'user_id': user.user_id,
                    'username': user.username,
                    'email': user.email
                }
            )
            result.append(task_detail)
        return result
    
    @staticmethod
    async def create_task(user: User, task_data: TaskCreate) -> TaskDetail:
        task = Task(**task_data.model_dump(), owner=user)
        created_task = await task.insert()
        return TaskDetail(
            task_id=created_task.task_id,
            title=created_task.title,
            description=created_task.description,
            status=created_task.status,
            created_at=created_task.created_at,
            updated_at=created_task.updated_at,
            owner={
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email
            }
        )
    
    @staticmethod
    async def detail(user:User, task_id: UUID):
        task = await Task.find_one(Task.task_id == task_id, Task.owner.id == user.id)
        if not task:
            return None
        return TaskDetail(
            task_id=task.task_id,
            title=task.title,
            description=task.description,
            status=task.status,
            created_at=task.created_at,
            updated_at=task.updated_at,
            owner={
                'user_id': user.user_id,
                'username': user.username,
                'email': user.email
            }
        )
    @staticmethod
    async def update_task(user: User, task_id: UUID, task_data: TaskUpdate):
        task = await Task.find_one(Task.task_id == task_id, Task.owner.id == user.id)
        if not task:
            return None
        
        update_data = task_data.model_dump(exclude_unset=True, exclude_none=True)
        if update_data:
            await task.update({'$set': {**update_data, 'updated_at': datetime.now(timezone.utc)}})
            await task.save()
        return TaskUpdate(
            title=task.title,
            description=task.description,
            status=task.status
        )
    
    @staticmethod
    async def delete_task(user: User, task_id: UUID) -> bool:
        task = await Task.find_one(Task.task_id == task_id, Task.owner.id == user.id)
        if task:
            await task.delete()
            return True
        return False