from fastapi import FastAPI, APIRouter

from .routes.auth import router as auth_router
from .routes.filestorage import router as filestorage_router
from .routes.object_agg import router as object_router
from .routes.objects_list import router as objects_list_router
from .routes.objects_tree import router as objects_tree_router
from .routes.objects_crud import router as objects_crud_router


app = FastAPI()

base_router = APIRouter(prefix="/api")

base_router.include_router(auth_router)
base_router.include_router(filestorage_router)
base_router.include_router(object_router)
base_router.include_router(objects_list_router)
base_router.include_router(objects_tree_router)
base_router.include_router(objects_crud_router)

app.include_router(base_router)
