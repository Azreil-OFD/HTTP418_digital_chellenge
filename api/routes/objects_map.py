from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.db import get_session

router = APIRouter(tags=["objects"])


@router.get("/objects/map")
async def objects_map(
    session: AsyncSession = Depends(get_session),
):
    query = text("""
        SELECT 
            o.id,
            o.name,
            oc.lat,
            oc.lon 
        FROM objects_coordinates oc
        LEFT JOIN objects o ON o.id = oc.id
        ORDER BY o.name;
    """)

    result = (await session.execute(query, {})).fetchall()
    if not result:
        return []

    return [
        {
            "id": row[0],
            "name": row[1],
            "coordinates": {
                "lat": row[2],
                "lon": row[3]
            }
        } for row in result
    ]
