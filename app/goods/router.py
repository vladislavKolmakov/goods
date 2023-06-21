from fastapi import APIRouter
from app.goods.dao import GoodsDAO
from app.goods.models import Goods
from app.goods.schemas import SGoods


router = APIRouter(
    prefix='/goods',
    tags=['Goods'],
)




@router.post('/add_goods')
async def add_goods():
    return await GoodsDAO.add(name='bred', count=13, price=57)
# async def add_goods(data: Goods):
#     await GoodsDAO.add(data)
