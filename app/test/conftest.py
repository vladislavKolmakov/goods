import asyncio
import json
import pytest
from sqlalchemy import insert
from app.database import Base, async_session_maker, engine

from app.database import MODE
from app.goods.models import Goods


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        def open_mock_json(model: str):
            with open(f'app/test/mock_{model}.json', 'r') as file:
                return json.load(file)

    goods = open_mock_json('goods')

    async with async_session_maker() as session:
        add_hotels = insert(Goods).values(goods)
        await session.execute(add_hotels)
        await session.commit()


# Взято из документации к pytest-asyncio
# Создаем новый event loop для прогона тестов
@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
