from fastapi import FastAPI, APIRouter

from .routes.auth import router as auth_router
from .routes.filestorage import router as filestorage_router
from .routes.object import router as object_router


app = FastAPI()

base_router = APIRouter(prefix="/api")

base_router.include_router(auth_router)
base_router.include_router(filestorage_router)
base_router.include_router(object_router)

app.include_router(base_router)
