from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Float, Date, UniqueConstraint, MetaData, Table
from sqlalchemy.orm import relationship

from api.database.db import Base, get_session, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    password_hash = Column(String)


metadata = MetaData()

TABLES = {
    "objects": None,
    "wells": None,
    "well_day_histories": None,
    "well_day_plans": None,
}


async def load_tables():
    """Загружает таблицы и сохраняет их в глобальном словаре."""
    async with engine.connect() as conn:
        await conn.run_sync(metadata.reflect)
        for table_name in TABLES.keys():
            TABLES[table_name] = metadata.tables[table_name]


async def ensure_tables_loaded():
    """Гарантирует, что таблицы загружены."""
    if any(value is None for value in TABLES.values()):
        await load_tables()


def get_table(name: str) -> Table:
    """Возвращает таблицу по имени, если она загружена."""
    if TABLES[name] is None:
        raise RuntimeError(f"Table '{name}' is not loaded. Ensure `load_tables()` is called.")
    return TABLES[name]
