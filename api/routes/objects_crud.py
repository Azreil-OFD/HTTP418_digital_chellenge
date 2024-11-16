from fastapi import APIRouter, Depends, Query, HTTPException, Path
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.db import get_session

router = APIRouter(tags=["objects"])


@router.get("/objects/object/{obj_id}")
async def get_object_by_id(
        obj_id: int = Path(..., description="Object ID"),
        session: AsyncSession = Depends(get_session),
):
    result = await session.execute(text("""
        SELECT objects.id, objects.name, objects_type.name as type
        FROM objects
        LEFT JOIN objects_type ON objects.id = objects_type.id
        WHERE objects.id = :obj_id
    """), {"obj_id": obj_id})

    obj = result.fetchone()
    if not obj:
        raise HTTPException(status_code=404, detail="No area found")

    return {"id": obj[0], "name": obj[1], "type": obj[2]}
