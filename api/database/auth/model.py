from sqlalchemy import Column, Integer, String
from ..db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    password_hash = Column(String)
