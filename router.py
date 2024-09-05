from typing import Annotated

from fastapi import Depends, APIRouter

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.post("")
async def create_task(request: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_task(request)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
