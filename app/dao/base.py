from app.database import async_session_maker
from sqlalchemy import insert


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
