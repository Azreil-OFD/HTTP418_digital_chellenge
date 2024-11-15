from fastapi import FastAPI, APIRouter

from api.database.db import create_db_and_tables
from .routes.auth import router as auth_router
from .routes.orders import router as order_router


app = FastAPI()

base_router = APIRouter(prefix="/api")

base_router.include_router(auth_router)
base_router.include_router(order_router)

app.include_router(base_router)


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()
