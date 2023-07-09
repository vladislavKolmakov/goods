from app.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    name = Column(String)
    second_name = Column(String)
    surname = Column(String)
    hashed_password = Column(String)
    email = Column(String)
    compaign_id = Column(Integer)
