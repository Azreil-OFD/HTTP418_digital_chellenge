import pprint

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import or_, Date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import cast
from sqlalchemy.types import Integer, String
from typing import List, Optional
from api.database.db import get_session
from api.database.model import get_table

router = APIRouter(tags=["objects"])

VALID_TYPES = {"well", "ngdu", "cdng", "kust", "mest"}
VALID_ORDER_FIELDS = {"name", "debit", "ee_consume", "expenses", "pump_operating"}
VALID_ORDER_DIRECTIONS = {"asc", "desc"}
VALID_MODES = {"history", "plan"}


@router.get("/api/objects/search/")
async def search_objects(
    obj_id: int = Query(..., description="Object id"),
    order_field: str = Query("name", description="Field to order by", example="name"),
    order_direction: str = Query("asc", description="Order direction (asc or desc)", example="asc"),
    page: int = Query(1, ge=1, description="Page number", example=1),
    per_page: int = Query(50, ge=1, le=100, description="Number of items per page", example=50),
    date_from: Optional[str] = Query(None, description="Start date (YYYY-MM-DD)", example="2024-12-31"),
    date_to: Optional[str] = Query(None, description="End date (YYYY-MM-DD)", example="2024-12-31"),
    mode: str = Query("history", description="Mode (history or plan)", example="history"),

    session: AsyncSession = Depends(get_session),
):
    if order_field not in VALID_ORDER_FIELDS:
        raise HTTPException(status_code=400, detail=f"Invalid order_field. Valid fields: {', '.join(VALID_ORDER_FIELDS)}")
    if order_direction not in VALID_ORDER_DIRECTIONS:
        raise HTTPException(status_code=400, detail=f"Invalid order_direction. Valid directions: asc, desc")
    if mode not in VALID_MODES:
        raise HTTPException(status_code=400, detail=f"Invalid mode. Valid modes: history, plan")

    objects = get_table("objects")
    well_day_plans = get_table("well_day_plans")
    wells = get_table("wells")
    well_day_histories = get_table("well_day_histories")

    table = well_day_plans if mode == "history" else well_day_histories

    query_statement = (
        select(objects, table)
        .join(table, table.c.well == objects.c.id)
        .join(wells, wells.c.well == table.c.well)
        .where(or_(
            wells.c.well == obj_id,
            wells.c.ngdu == obj_id,
            wells.c.cdng == obj_id,
            wells.c.kust == obj_id,
            wells.c.mest == obj_id
        ))
    )

    if date_from:
        query_statement = query_statement.where(table.c.date_add >= cast(date_from, Date))
    if date_to:
        query_statement = query_statement.where(table.c.date_add <= cast(date_to, Date))

    if order_field in VALID_ORDER_FIELDS:
        order_column = getattr(table.c, order_field, None)
        if order_column is not None:
            if order_direction == "desc":
                order_column = order_column.desc()
            query_statement = query_statement.order_by(order_column)

    offset = (page - 1) * per_page
    query_statement = query_statement.offset(offset).limit(per_page)

    result = await session.execute(query_statement)
    records = result.fetchall()

    pprint.pprint(records)

@router.get("/objects/get_area")
async def get_area(session: AsyncSession = Depends(get_session)):
    objects_table = get_table("objects")

    query = select(objects_table.c.id, objects_table.c.name).where(objects_table.c.type == 1)
    # print("lffasdasddas")
    area = await session.execute(query)
    if not area:
        raise HTTPException(status_code=404, detail="No area found")
    objects = area.fetchall()

    return [{"id": obj.id, "name": obj.name} for obj in objects]