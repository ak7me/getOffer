from .db_setup import connection
from .models import User, Vacancy, Filter
from sqlalchemy import select

async def set_user(session, id: int, username: str):