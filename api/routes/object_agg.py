from fastapi import APIRouter, Depends, Query, HTTPException, Path
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.db import get_session

router = APIRouter(tags=["objects"])

VALID_ORDER_FIELDS = {"date_add", "debit", "ee_consume", "expenses", "pump_operating"}
VALID_ORDER_DIRECTIONS = {"asc", "desc"}
VALID_MODES = {"history", "plan"}


@router.get("/objects/search/")
async def search_objects(
    obj_id: int = Query(..., description="Object id"),
    order_field: str = Query("date_add", description="Field to order by", example="date_add"),
    order_direction: str = Query("asc", description="Order direction (asc or desc)", example="asc"),
    page: int = Query(1, ge=1, description="Page number", example=1),
    per_page: int = Query(50, ge=1, le=100, description="Number of items per page", example=50),
    mode: str = Query("history", description="Mode (history or plan)", example="history"),

    session: AsyncSession = Depends(get_session),
):
    if order_field not in VALID_ORDER_FIELDS:
        raise HTTPException(status_code=400, detail=f"Invalid order_field. Valid fields: {', '.join(VALID_ORDER_FIELDS)}")
    if order_direction not in VALID_ORDER_DIRECTIONS:
        raise HTTPException(status_code=400, detail=f"Invalid order_direction. Valid directions: asc, desc")
    if mode not in VALID_MODES:
        raise HTTPException(status_code=400, detail=f"Invalid mode. Valid modes: history, plan")

    query = text(f"""
        SELECT date_add,
               sum(debit) as debit,
               sum(ee_consume) as ee_consume,
               sum(expenses) as expenses,
               sum(pump_operating) as pump_operating
        FROM {'well_day_histories' if mode == 'history' else 'well_day_plans'}
        WHERE well IN (SELECT well
                       FROM wells
                       WHERE well = :obj_id
                          OR ngdu = :obj_id
                          OR cdng = :obj_id
                          OR kust = :obj_id
                          OR mest = :obj_id)
        GROUP BY date_add
        ORDER BY {order_field} {'asc' if order_direction == 'asc' else 'desc'}
        LIMIT :limit OFFSET :offset;
    """)

    result = await session.execute(query, {
        "obj_id": obj_id,
        "limit": per_page,
        "offset": per_page*page
    })

    total_count = (await session.execute(
        text(f"""
        SELECT count(*) FROM {'well_day_histories' if mode == 'history' else 'well_day_plans'}
        WHERE well IN (
           SELECT well
           FROM wells
           WHERE well = :obj_id
              OR ngdu = :obj_id
              OR cdng = :obj_id
              OR kust = :obj_id
              OR mest = :obj_id)
        GROUP BY date_add"""), {"obj_id": obj_id}
    )).fetchone()[0]

    return {
        "meta": {
            "total_count": total_count,
            "total_page": total_count//per_page + (1 if total_count % per_page > 0 else 0),
            "current_page": page
        },
        "data": [
            {
                "date": row[0],
                "debit": row[1],
                "ee_consume": row[2],
                "expenses": row[3],
                "pump_operating": row[4],
            } for row in result.fetchall()
        ]
    }


@router.get("/objects/get_area")
async def get_area(session: AsyncSession = Depends(get_session)):
    query = text("""
        SELECT id, name
        FROM objects
        WHERE type = :type
    """)
    
    result = await session.execute(query, {"type": 1})
    
    objects = result.fetchall()

    if not objects:
        raise HTTPException(status_code=404, detail="No area found")

    return [{"id": obj[0], "name": obj[1]} for obj in objects]

