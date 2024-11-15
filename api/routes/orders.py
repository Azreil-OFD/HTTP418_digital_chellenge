import uuid

from fastapi import Depends, UploadFile, APIRouter, Form, File
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from api.database.db import get_session

class CreateOrderResponse(BaseModel):
    order_id: uuid.UUID


router = APIRouter(tags=["orders"])


@router.post("/create_order/", response_model=CreateOrderResponse)
async def create_order(
        title: str = Form(..., min_length=3, max_length=255),
        description: str = Form(..., max_length=1024),
        image: UploadFile = File(...),
    session: AsyncSession = Depends(get_session)
):
    # image_filename = f"{request.title.replace(' ', '_')}.jpg"
    # with open(f"images/{image_filename}", "wb") as f:
    #     f.write(await request.image.read())
    #
    # # Создание нового заказа
    # new_order = Order(
    #     title=request.title,
    #     description=request.description,
    #     image_url=f"/images/{image_filename}"
    # )
    # session.add(new_order)
    # await session.commit()
    # await session.refresh(new_order)

    return CreateOrderResponse(order_id=str(uuid.uuid4()))
