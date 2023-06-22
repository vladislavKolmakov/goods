from fastapi import APIRouter
from app.goods.dao import GoodsDAO
from app.goods.models import Goods
from app.goods.schemas import SGoods


router = APIRouter(
    prefix='/goods',
    tags=['Goods'],
)


@router.post('/add_goods')
async def add_goods(data: SGoods):
    await GoodsDAO.add(name=data.name, count=data.count, price=data.price)


@router.get('/get_goods')
async def get_goods(name: str = None, count: int = None, price: int = None):
    return await GoodsDAO.find_by_filter(name=name)
