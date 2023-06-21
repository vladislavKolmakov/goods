from pydantic import BaseModel


class SGoods(BaseModel):
    id: int
    name: str
    cont: int
    ptice: int

    class Config:
        orm_mode = True
