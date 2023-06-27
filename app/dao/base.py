from app.database import async_session_maker
from sqlalchemy import insert, select, update, delete


class BaseDAO:
    model = None

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def find_one_or_none(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def update_row(cls, id: int, **data):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == id).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, name: str):
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.name == name)
            await session.execute(query)
            await session.commit()
