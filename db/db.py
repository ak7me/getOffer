from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

DB_URL = "sqlite+aiosqlite:///topovaya.db"

engine = create_async_engine(DB_URL)
session = create_async_engine(engine)

class Base(DeclarativeBase):
    pass