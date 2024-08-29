from tokenize import String

from sqlalchemy import Integer
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedColumn

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db", echo=True
)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):
    __tablename__ = "tasks"

    id = MappedColumn(Integer, primary_key=True, autoincrement=True)
    name = MappedColumn(String)
    description = MappedColumn(String, nullable=True)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
