from pydantic import BaseModel


class SGoods(BaseModel):
    # id: int
    name: str
    count: int
    price: int

    class Config:
        orm_mode = True
