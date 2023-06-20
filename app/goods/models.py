from sqlalchemy import Column, Integer, String

class Goods():
    __tablename__  = 'goods'

    id = Column(Integer, primary_key=True)
    name = Column(String, nulable=False)
    count = Column(Integer, nulable=False)
    count = Column(Integer, nulable=False)