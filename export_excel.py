from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi.responses import FileResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import pandas as pd
from api.database.db import get_session

router = APIRouter(tags=["export_excel"])

# Рекурсивный SQL-запрос для получения иерархии
HIERARCHY_QUERY = """
WITH RECURSIVE hierarchy AS (
    SELECT id, type
    FROM objects
    WHERE id = :object_id
    UNION ALL
    SELECT o.id, o.type
    FROM objects o
    INNER JOIN hierarchy h ON o.parent_id = h.id
)
SELECT id FROM hierarchy;
"""

# SQL-запрос для выборки всех данных
SQL_QUERY = """
SELECT
    date_fact,
    well,
    debit,
    ee_consume,
    expenses,
    pump_operating
FROM well_day_histories
WHERE well IN (
    SELECT id FROM wells WHERE wells.object_id IN (
        SELECT id FROM hierarchy
    )
)
ORDER BY date_fact;
"""

OUTPUT_FILE = "well_day_histories.xlsx"

@router.get("/well_day_histories/download/{object_id}")
async def download_well_day_histories(
    object_id: int = Path(..., description="ID of the object"),
    session: AsyncSession = Depends(get_session),
):
    """
    Делает выборку всех данных из таблицы well_day_histories для указанного объекта и сохраняет в Excel файл.
    """
    try:
        await session.execute(text(HIERARCHY_QUERY), {"object_id": object_id})

        result = await session.execute(text(SQL_QUERY))
        data = result.fetchall()

        if not data:
            raise HTTPException(status_code=404, detail="No data found for the given object.")

        df = pd.DataFrame(data, columns=["date_fact", "well", "debit", "ee_consume", "expenses", "pump_operating"])

    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing data: {str(e)}")

    return FileResponse(
        path=df.to_excel(OUTPUT_FILE, index=False, engine="openpyxl"),
        filename=f"well_day_histories_{object_id}.xlsx"
    )
