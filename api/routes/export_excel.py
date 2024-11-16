from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from fastapi.responses import FileResponse
import pandas as pd
from io import BytesIO
from api.database.db import get_session

router = APIRouter(tags=["export_excel"])

@router.get("/objects/export/{object_id}")
async def export_object_data(
    object_id: int = Path(..., description="ID of the object"),
    session: AsyncSession = Depends(get_session)
):
    try:
        # Step 1: Get the object type
        object_type_query = text("SELECT type FROM objects WHERE id = :object_id")
        result = await session.execute(object_type_query, {'object_id': object_id})
        object_type_row = result.fetchone()
        if not object_type_row:
            raise HTTPException(status_code=404, detail="Object not found.")
        object_type = object_type_row[0]

        # Step 2: Define hierarchy levels and mapping
        hierarchy_levels = ['mest', 'ngdu', 'cdng', 'kust', 'well']
        type_to_levels = {
            'mest': ['mest', 'ngdu', 'cdng', 'kust', 'well'],
            'ngdu': ['ngdu', 'cdng', 'kust', 'well'],
            'cdng': ['cdng', 'kust', 'well'],
            'kust': ['kust', 'well'],
            'well': ['well']
        }

        levels_to_process = type_to_levels.get(object_type)
        if not levels_to_process:
            raise HTTPException(status_code=400, detail="Invalid object type.")

        object_type_column = object_type  # The column in 'wells' table that matches the object_type

        excel_data = {}

        # Step 3: Process both tables
        for table_name in ['well_day_histories', 'well_day_plans']:
            for level in levels_to_process:
                # Generate the appropriate query
                if level == 'well' and object_type == 'well':
                    # No aggregation needed
                    query = f"""
                        SELECT date, debit, ee_consume, expenses, pump_operating
                        FROM {table_name}
                        WHERE well = :object_id
                        ORDER BY date;
                    """
                    params = {'object_id': object_id}
                    columns = ['date', 'debit', 'ee_consume', 'expenses', 'pump_operating']
                    sheet_name = f"{object_type}_{object_id}_{table_name}_{level}"
                elif level == 'well':
                    # Get data per well without aggregation
                    query = f"""
                        SELECT WH.date, W.well, WH.debit, WH.ee_consume, WH.expenses, WH.pump_operating
                        FROM {table_name} WH
                        JOIN wells W ON WH.well = W.well
                        WHERE W.{object_type_column} = :object_id
                        ORDER BY WH.date, W.well;
                    """
                    params = {'object_id': object_id}
                    columns = ['date', 'well', 'debit', 'ee_consume', 'expenses', 'pump_operating']
                    sheet_name = f"{object_type}_{object_id}_{table_name}_{level}"
                else:
                    # Aggregate data at the current level
                    query = f"""
                        SELECT WH.date, W.{level}, SUM(WH.debit) AS debit, SUM(WH.ee_consume) AS ee_consume,
                               SUM(WH.expenses) AS expenses, SUM(WH.pump_operating) AS pump_operating
                        FROM {table_name} WH
                        JOIN wells W ON WH.well = W.well
                        WHERE W.{object_type_column} = :object_id
                        GROUP BY WH.date, W.{level}
                        ORDER BY WH.date, W.{level};
                    """
                    params = {'object_id': object_id}
                    columns = ['date', level, 'debit', 'ee_consume', 'expenses', 'pump_operating']
                    sheet_name = f"{object_type}_{object_id}_{table_name}_{level}"

                # Execute the query
                data_result = await session.execute(text(query), params)
                data = data_result.fetchall()

                # If data exists, add to Excel
                if data:
                    df = pd.DataFrame(data, columns=columns)
                    # Limit sheet name to 31 characters (Excel limitation)
                    excel_data[sheet_name[:31]] = df

        if not excel_data:
            raise HTTPException(status_code=404, detail="No data found for the specified object.")

        # Step 4: Create the Excel file
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            for sheet_name, df in excel_data.items():
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        output.seek(0)

        # Step 5: Return the Excel file as a response
        return FileResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            filename=f"object_data_{object_id}.xlsx"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
