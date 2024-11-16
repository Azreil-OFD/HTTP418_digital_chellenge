from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.db import get_session

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
               sum(debit),
               sum(ee_consume),
               sum(expenses),
               sum(pump_operating)
        FROM well_day_histories
        WHERE well IN (SELECT well
                       FROM wells
                       WHERE well = :obj_id
                          OR ngdu = :obj_id
                          OR cdng = :obj_id
                          OR kust = :obj_id
                          OR mest = :obj_id)
        GROUP BY date_add
        ORDER BY date_add
        LIMIT :limit OFFSET :offset;
    """)

    result = await session.execute(query, {
        "obj_id": obj_id,
        "limit": per_page,
        "offset": per_page*page
    })

    return [
        {
            "date": row[0],
            "debit": row[1],
            "ee_consume": row[2],
            "expenses": row[3],
            "pump_operating": row[4],
        } for row in result.fetchall()
    ]


@router.get("/api/objects/tree/")
async def search_objects(
    obj_id: int = Query(..., description="Object id"),
    session: AsyncSession = Depends(get_session),
):
    result_tree = (await session.execute(
        text("""
            SELECT 
                ngdu,
                cdng,
                kust,
                well
            FROM wells
            WHERE ngdu = :obj_id;
        """), {"obj_id": obj_id})).fetchall()

    if not result_tree:
        raise HTTPException(status_code=404, detail="No data found for the given obj_id.")

    uniq_ids = set()
    mest_groups = {}

    for row in result_tree:
        ngdu, cdng, kust, well = row

        if ngdu not in mest_groups:
            mest_groups[ngdu] = {}
        if cdng not in mest_groups[ngdu]:
            mest_groups[ngdu][cdng] = {}
        if kust not in mest_groups[ngdu][cdng]:
            mest_groups[ngdu][cdng][kust] = []

        mest_groups[ngdu][cdng][kust].append(well)
        uniq_ids.update([ngdu, cdng, kust])

    objects_map = {}
    for row in (await session.execute(
        text("SELECT id, name, type FROM objects WHERE id = ANY(:ids)"),
        {"ids": list(uniq_ids)}
    )).fetchall():
        objects_map[row[0]] = {"name": row[1]}

    ngdu_node = {
        "key": "0",
        "type": "main",
        "data": {
            "name": objects_map.get(obj_id, {}).get("name", "Месторождение"),
        },
        "children": [],
    }

    for ngdu, cdngs in mest_groups.items():
        ngdu_node = {
            "key": ngdu,
            "type": "main",
            "data": {
                "name": objects_map.get(ngdu, {}).get("name", f"Цех {ngdu}"),
            },
            "children": [],
        }
        for cdng, kusts in cdngs.items():
            cdng_node = {
                "key": cdng,
                "type": "workshop",
                "data": {
                    "name": objects_map.get(cdng, {}).get("name", f"ЦДНГ {cdng}"),
                },
                "children": [],
            }
            ngdu_node["children"].append(cdng_node)
            for kust, wells in kusts.items():
                kust_node = {
                    "key": kust,
                    "type": "bush",
                    "data": {
                        "name": objects_map.get(kust, {}).get("name", f"Куст {kust}"),
                    },
                    "children": [],
                }
                cdng_node["children"].append(kust_node)

    return ngdu_node

