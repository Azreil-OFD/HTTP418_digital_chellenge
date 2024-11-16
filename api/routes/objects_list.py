from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.db import get_session

router = APIRouter(tags=["objects"])

VALID_ORDER_DIRECTIONS = {"asc", "desc"}

OBJECT_TYPES = {
    "mest": 1,
    "cdng": 2,
    "kust": 3,
    "wells": 4,
    "ngdu": 5,
}


@router.get("/objects/list")
async def objects_list(
        order_direction: str = Query("asc", description="Order direction (asc or desc)", example="asc"),
        obj_type: str = Query("wells", description="Object type", example="wells"),
        page: int = Query(1, ge=1, description="Page number", example=1),
        per_page: int = Query(50, ge=1, le=100, description="Number of items per page", example=50),

        session: AsyncSession = Depends(get_session),
):
    if order_direction not in VALID_ORDER_DIRECTIONS:
        raise HTTPException(status_code=400, detail=f"Invalid order_direction. Valid directions: asc, desc")
    if obj_type not in OBJECT_TYPES:
        raise HTTPException(status_code=400, detail=f"Invalid obj_type")

    query = text(f"""
        SELECT o.id as id, o.name as name, ot.name as type
        FROM objects o
            LEFT JOIN objects_type ot ON o.type = ot.id
        WHERE o.type = {OBJECT_TYPES.get(obj_type, 4)}
        ORDER BY o.name {'asc' if order_direction == 'asc' else 'desc'}
        LIMIT :limit OFFSET :offset;
    """)

    result = await session.execute(query, {
        "limit": per_page,
        "offset": per_page * (page - 1)
    })

    total_count = (await session.execute(
        text(f"SELECT count(*) FROM objects WHERE type = {OBJECT_TYPES.get(obj_type, 4)}"), {}
    )).fetchone()[0]

    return {
        "meta": {
            "total_count": total_count,
            "total_page": total_count//per_page + (1 if total_count % per_page > 0 else 0),
            "current_page": page
        },
        "data": [
            {
                "id": row[0],
                "name": row[1],
                "type": row[2],
            } for row in result.fetchall()
        ]
    }

