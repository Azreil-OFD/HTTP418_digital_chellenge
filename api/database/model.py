from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Float, Date, UniqueConstraint, MetaData, Table
from sqlalchemy.orm import relationship

from api.database.db import Base, get_session, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    password_hash = Column(String)
