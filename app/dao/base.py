from app.database import async_session_maker
from sqlalchemy import insert, select


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()


    @classmethod
    async def find_by_filter(cls, **filter):
        async with async_session_maker() as sesion:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            result = await sesion.execute(query)
            print(query)
            return result.mappings().all()
