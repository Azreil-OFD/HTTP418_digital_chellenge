import bcrypt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

from api.config import JWT_SECRET_KEY


def create_jwt_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
    }
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm="HS256")


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())


def get_user_id(credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer())) -> int:
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        raise HTTPException(status_code=401, detail="Invalid token")