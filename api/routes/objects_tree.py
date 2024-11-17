from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from api.database.db import get_session
from api.routes.utils.security import get_user_id

router = APIRouter(tags=["objects"])


def calculate_counts(node):
    if "children" in node and node["children"]:
        count = 0
        for child in node["children"]:
            count += calculate_counts(child)
        node["data"]["counts"] = count
        return count
    else:
        return 1


@router.get("/objects/tree/")
async def objects_tree(
    obj_id: int = Query(..., description="Object id"),
    session: AsyncSession = Depends(get_session),
    _: int = Depends(get_user_id),
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
                for well in wells:
                    well_node = {
                        "key": well,
                        "type": "well",
                        "data": {
                            "name": objects_map.get(well, {}).get("name", f"Скважина {well}"),
                        },
                    }
                    kust_node["children"].append(well_node)

    calculate_counts(ngdu_node)

    return ngdu_node
