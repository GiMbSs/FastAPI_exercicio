from fastapi import APIRouter, Depends, HTTPException, status
from schemas.task_schema import TaskDetail, TaskCreate, TaskUpdate
from models.user_model import User
from api.depedencies.user_deps import get_current_user
from services.task_service import TaskService
from models.task_model import Task
from typing import List
from uuid import UUID



task_router = APIRouter()

@task_router.get('/', summary='Lista de tarefas', response_model=List[TaskDetail])
async def list_tasks(user: User = Depends(get_current_user)):
    return await TaskService.list_tasks(user)

@task_router.get('/{task_id}', summary='Detalhes de uma tarefa', response_model=TaskDetail)
async def get_task_detail(task_id: str, user: User = Depends(get_current_user)):
    try:
        task_uuid = UUID(task_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='ID da tarefa inválido'
        )
    
    task_detail = await TaskService.detail(user, task_uuid)
    if not task_detail:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tarefa não encontrada'
        )
    return task_detail

@task_router.post('/create', summary='Cria uma nova tarefa', response_model=TaskDetail)
async def create_task(task_data: TaskCreate, user: User = Depends(get_current_user)):
    return await TaskService.create_task(user, task_data)

@task_router.put('/{task_id}', summary='Atualiza uma tarefa', response_model=TaskUpdate)
async def update_task(task_id: str, task_data: TaskUpdate, user: User = Depends(get_current_user)):
    try:
        task_uuid = UUID(task_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='ID da tarefa inválido'
        )
    
    updated_task = await TaskService.update_task(user, task_uuid, task_data)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tarefa não encontrada'
        )
    return updated_task

@task_router.delete('/{task_id}', summary='Deleta uma tarefa')
async def delete_task(task_id: str, user: User = Depends(get_current_user)):
    try:
        task_uuid = UUID(task_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='ID da tarefa inválido'
        )
    
    deleted = await TaskService.delete_task(user, task_uuid)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Tarefa não encontrada'
        )
    return {'detail': 'Tarefa deletada com sucesso'}