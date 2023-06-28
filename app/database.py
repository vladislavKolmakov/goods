from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import os
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv

load_dotenv()

MODE = os.getenv('MODE')
# from app.config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME

if MODE == "TEST":
    DATABASE_URL = 'postgresql+asyncpg://postgres:123@localhost:5432/test_goods_db'
    DATABASE_PARAMS = {'poolclass': NullPool}
else:
    DATABASE_URL = 'postgresql+asyncpg://postgres:123@localhost:5432/Goods'
    DATABASE_PARAMS = {}

print(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
