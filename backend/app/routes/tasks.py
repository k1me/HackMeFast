from fastapi import APIRouter, HTTPException
from app.services.task_service import get_tasks_by_category, get_task_by_id

router = APIRouter()

@router.get("/tasks")
async def get_tasks(category: str = None):
    tasks = get_tasks_by_category(category)
    return tasks

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, details="Task not found")
    return task