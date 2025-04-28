'''Database connection related functions.'''
from typing import Annotated
from fastapi import Depends
from models import *
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.ext.asyncio import AsyncEngine
from config import Config

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


engine = AsyncEngine(
    create_engine(
        url = Config.DATABASE_URL,
        echo = True
))

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)