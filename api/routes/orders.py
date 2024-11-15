import uuid

from fastapi import Depends, UploadFile, APIRouter, Form, File, HTTPException, Path
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from api.config import FILESTORAGE_PATH
from api.database.db import get_session
from api.database.model import Order

from api.routes.utils.security import get_user_id

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif"}


class CreateOrderResponse(BaseModel):
    order_id: uuid.UUID


router = APIRouter(tags=["orders"])


@router.post("/create_order/", response_model=CreateOrderResponse)
async def create_order(
    title: str = Form(..., min_length=3, max_length=255),
    description: str = Form(..., max_length=1024),
    image: UploadFile = File(...),
    session: AsyncSession = Depends(get_session),
    user_id: int = Depends(get_user_id),
):
    filename = image.filename.lower()
    if not any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        raise HTTPException(
            status_code=400,
            detail="Invalid file extension. Allowed: .jpg, .jpeg, .png, .gif"
        )

    content = await image.read()
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds the limit of {MAX_FILE_SIZE // 1024 // 1024} MB"
        )

    image_uuid = str(uuid.uuid4())
    order_uuid = str(uuid.uuid4())

    image_filename = f"{image_uuid}.{filename.split('.')[-1]}"
    with open(f"{FILESTORAGE_PATH}/{image_filename}", "wb") as f:
        f.write(content)

    new_order = Order(
        uuid=order_uuid,
        title=title,
        description=description,
        image_name=image_filename,
        user_id=user_id,
    )
    session.add(new_order)
    await session.commit()

    return CreateOrderResponse(order_id=order_uuid)


class GetOrderResponse(BaseModel):
    order_id: uuid.UUID
    image_name: str
    title: str
    description: str


@router.get("/get_order/{order_id}")
async def get_order(
    order_id: uuid = Path(..., description="Order UUID"),
    user_id: int = Depends(get_user_id),
    session: AsyncSession = Depends(get_session),
) -> GetOrderResponse:
    query = select(Order).where(
        Order.uuid == order_id,
        Order.user_id == user_id
    )

    result = await session.execute(query)
    order = result.scalars().first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return GetOrderResponse(
        order_id=order.uuid,
        image_name=f"api/files/{order.image_name}",
        title=order.title,
        description=order.description
    )