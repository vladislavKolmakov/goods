from fastapi import APIRouter
from app.goods.dao import GoodsDAO
# from app.goods.models import Goods
from app.goods.schemas import SGoods


router = APIRouter(
    prefix='/goods',
    tags=['Goods'],
)


@router.post('/add_goods')
async def add_goods(data: SGoods):
    item = await GoodsDAO.find_one_or_none(name=data.name)
    # print(data.name)
    if item:
        await GoodsDAO.update_row(id=item.id, name=data.name, count=data.count, price=data.price)
        print('item.id')
        print('upd')
    else:
        # await GoodsDAO.add(name=data.name, count=data.count, price=data.price)
        print('add')


@router.get('/get_goods')
async def get_goods(name: str = None, count: int = None, price: int = None):
    return await GoodsDAO.find_by_filter(name, count, price)
