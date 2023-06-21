from sqlalchemy import Column, Integer, String
from app.database import Base


class Goods(Base):
    __tablename__  = 'goods'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    count = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
