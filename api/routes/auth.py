import bcrypt
import jwt
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.config import JWT_SECRET_KEY
from api.database.auth.model import User
from api.database.db import get_session


def create_jwt_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
    }
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


router = APIRouter(tags=["auth"])


class Request(BaseModel):
    login: EmailStr
    password: str = Field(min_length=5)


class Response(BaseModel):
    token: str


@router.post("/registration/")
async def register_handler(req: Request, session: AsyncSession = Depends(get_session)) -> Response:
    user = (await session.execute(select(User).where(User.login == req.login.lower()))).scalar()
    if user:
        raise HTTPException(status_code=400, detail="login already exists")

    new_user = User(login=req.login, password_hash=hash_password(req.password))
    session.add(new_user)

    await session.commit()
    await session.refresh(new_user)

    return Response(token=create_jwt_token(new_user.id))


@router.post("/authorization/")
async def authenticate_handler(req: Request, session: AsyncSession = Depends(get_session)) -> Response:
    user = (await session.execute(select(User).where(User.login == req.login.lower()))).scalar()
    if not user:
        raise HTTPException(status_code=403)

    if not verify_password(req.password, user.password_hash):
        raise HTTPException(status_code=403)

    return Response(token=create_jwt_token(user.id))