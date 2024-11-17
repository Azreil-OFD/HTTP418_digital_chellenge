from fastapi import APIRouter, Depends, Query, HTTPException, Path
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.db import get_session
from api.routes.utils.security import get_user_id

router = APIRouter(tags=["objects"])


@router.get("/objects/object/{obj_id}")
async def get_object_by_id(
    obj_id: int = Path(..., description="Object ID"),
    session: AsyncSession = Depends(get_session),
    _: int = Depends(get_user_id),
):
    result = await session.execute(text("""
        SELECT o.id, o.name, ot.name as type
        FROM objects o 
        LEFT JOIN objects_type ot ON o.type = ot.id
        WHERE o.id = :obj_id
    """), {"obj_id": obj_id})

    obj = result.fetchone()
    if not obj:
        raise HTTPException(status_code=404, detail="No area found")

    return {"id": obj[0], "name": obj[1], "type": obj[2]}
