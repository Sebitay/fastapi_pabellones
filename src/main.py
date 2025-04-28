'''Root file which inits the FastAPI app'''

from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_db_and_tables


@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting...")
    await create_db_and_tables()
    yield
    print(f"Server has been stopped")

app = FastAPI(
    title="PabellonesAPI",
    lifespan=life_span,
)