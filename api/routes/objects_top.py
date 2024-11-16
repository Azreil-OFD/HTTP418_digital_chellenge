import datetime

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.db import get_session

router = APIRouter(tags=["objects"])

VALID_ORDER_FIELDS = {"debit", "ee_consume", "expenses", "pump_operating"}
VALID_ORDER_DIRECTIONS = {"asc", "desc"}


@router.get("/objects/tops/")
async def tops_objects(
        order_field: str = Query("debit", description="""Field to order by: {"debit", "ee_consume", "expenses", "pump_operating"}""", example="debit"),
        order_direction: str = Query("asc", description="Order direction (asc or desc)", example="asc"),
        date_from: datetime.date = Query(None, description="Date from", example="2024-01-01"),
        date_to: datetime.date = Query(None, description="Date to", example="2024-12-31"),
        counts: int = Query(10, le=100, description="tops count", example=10),

        session: AsyncSession = Depends(get_session),
):
    if order_field not in VALID_ORDER_FIELDS:
        raise HTTPException(status_code=400,
                            detail=f"Invalid order_field. Valid fields: {', '.join(VALID_ORDER_FIELDS)}")
    if order_direction not in VALID_ORDER_DIRECTIONS:
        raise HTTPException(status_code=400, detail=f"Invalid order_direction. Valid directions: asc, desc")

    today = datetime.date.today()
    if not date_from:
        date_from = today - datetime.timedelta(days=365)
    if not date_to:
        date_to = today

    query = text(f"""
        SELECT 
            o.id, 
            o.name,
            sum(wh.{order_field}) as val
        FROM well_day_histories wh
        LEFT JOIN objects o ON o.id = wh.well
        WHERE 
            wh.date_add >= :date_from AND wh.date_add <= :date_to
        GROUP BY o.id, o.name
        ORDER BY 
            val {'asc' if order_direction == 'asc' else 'desc'},
            o.name
        LIMIT :limit
    """)

    result = (await session.execute(query, {
        "date_from": date_from,
        "date_to": date_to,
        "limit": counts
    })).fetchall()

    return [
        {
            "id": row.id,
            "name": row.name,
            "value": row.val,
            "units": {
                "debit": "m³",
                "ee_consume": "kWh",
                "expenses": "c.u.",
                "pump_operating": "c.u."
            }.get(order_field, "c.u.")
        }
        for row in result
    ]
