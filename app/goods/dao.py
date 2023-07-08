from app.dao.base import BaseDAO
from app.goods.models import Goods
from app.database import async_session_maker
from sqlalchemy import select
from sqlalchemy.orm import Query


class GoodsDAO(BaseDAO):
    model = Goods

    # TODO rewrite to universal function userg *args or **kwargs
    @classmethod
    async def find_by_filter(cls, name: str = None, count: int = None, price: int = None):
        async with async_session_maker() as session:
            query: Query = select(Goods)
            if name:
                print(name)
                query = query.filter_by(name=name)

            if count:
                print(count)
                query = query.filter_by(count=count)

            if price:
                print(price)
                query = query.filter_by(price=price)

            result = await session.execute(query)
            print(query)
            return result.mappings().all()
