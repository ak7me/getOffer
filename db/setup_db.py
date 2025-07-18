from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

DB_URL = "sqlite+aiosqlite:///topovaya.db"

async_engine = create_async_engine(DB_URL)
async_session_maker = async_sessionmaker(async_engine)

class Base(DeclarativeBase): pass

def connection(func) -> function: # соединение
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            return await func(session, *args, **kwargs)
    return wrapper


async def create_tables() -> None: # таблицы будут создавать при /start но мне это не нравится (добавить alembic!!!)
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)