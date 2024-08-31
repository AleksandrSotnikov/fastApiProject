from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from database import drop_tables, create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await drop_tables()
    print("db clear")
    await create_tables()
    print("db create")
    yield
    print("server stop")


app = FastAPI(lifespan=lifespan)


class STaskCreate(BaseModel):
    name: str
    description: str | None = None


class STask(STaskCreate):
    id: int


tasks = []


@app.post("/tasks/")
async def create_task(request: Annotated[STaskCreate, Depends()]):
    tasks.append(request)
    return {"ok": True}


# http://127.0.0.1:8000/docs#/
# @app.get("/tasks")
# async def get_tasks():
#     task = Task(name="Task 1", description="Task 1")
#     return {"data": task}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
