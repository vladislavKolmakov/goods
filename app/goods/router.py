from fastapi import APIRouter
from app.goods.dao import GoodsDAO
from app.exeptions import NotFoundItemExeption, OkExeption
from app.goods.schemas import SGoods


router = APIRouter(
    prefix='/goods',
    tags=['Goods'],
)


@router.post('/add')
async def add_goods(data: SGoods):
    item = await GoodsDAO.find_one_or_none(name=data.name)
    if item:
        await GoodsDAO.update_row(id=item.id, name=data.name, count=data.count, price=data.price)
    else:
        await GoodsDAO.add(name=data.name, count=data.count, price=data.price)
    raise OkExeption


@router.get('/find')
async def get_goods(name: str = None, count: int = None, price: int = None):
    return await GoodsDAO.find_by_filter(name, count, price)


@router.get('/find_all')
async def get_all():
    return await GoodsDAO.find_all()


@router.delete('/delete')
async def delete_goods(name: str):
    item = await GoodsDAO.find_one_or_none(name=name)
    if item:
        return await GoodsDAO.delete(name)
    else:
        raise NotFoundItemExeption
