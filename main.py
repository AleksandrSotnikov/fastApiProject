from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import delete_tables, create_tables
from router import router as tasks_router


# http://127.0.0.1:8000/docs#/

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("db clear")
    await create_tables()
    print("db create")
    yield
    print("server stop")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
