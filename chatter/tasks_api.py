from typing import List
from fastapi import APIRouter, HTTPException, status
from chatter.models import Task, TaskIn
from chatter.db import tasks, database

router = APIRouter(tags=["Tasks API"])


@router.get("/", response_model=List[Task])
async def get_all_tasks():
    query = tasks.select()
    return await database.fetch_all(query)


@router.get("/{task_id}", response_model=Task)
async def get_one_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    task = await database.fetch_one(query)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task


@router.post("/", response_model=Task)
async def create_task(task: TaskIn):
    query = tasks.insert().values(**task.dict())
    last_record_id = await database.execute(query)
    return {**task.dict(), "id": last_record_id}


@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskIn):
    query = tasks.select().where(tasks.c.id == task_id)
    task_ = await database.fetch_one(query)
    if task_ is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )

    query = tasks.update().values(**task.dict()).where(tasks.c.id == task_id)
    await database.execute(query)


@router.delete("/{task_id}")
async def delete_task(task_id: int):
    query = tasks.select().where(tasks.c.id == task_id)
    task_ = await database.fetch_one(query)
    if task_ is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Task not found"
        )

    query = tasks.delete().where(tasks.c.id == task_id)
    await database.execute(query)
