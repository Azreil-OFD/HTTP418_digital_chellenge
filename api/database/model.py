from sqlalchemy import Column, Integer, String, UUID, ForeignKey
from sqlalchemy.orm import relationship

from api.database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    password_hash = Column(String)

    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")


class Order(Base):
    __tablename__ = "orders"

    uuid = Column(UUID, primary_key=True)
    image_name = Column(String)
    title = Column(String)
    description = Column(String)

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="orders")
