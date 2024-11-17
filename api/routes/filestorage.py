from pathlib import Path

from fastapi import HTTPException, Depends, APIRouter
from fastapi.responses import FileResponse

from api.config import FILESTORAGE_PATH
from api.routes.utils.security import get_user_id

router = APIRouter(tags=["filestorage"])

BASE_DIR = Path(FILESTORAGE_PATH)


@router.get("/files/{file_name:path}")
async def serve_file(
        file_name: str,
        _: int = Depends(get_user_id),
) -> FileResponse:
    file = BASE_DIR / file_name
    if not file.exists() or not file.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file)
