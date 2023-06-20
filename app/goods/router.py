from fastapi import APIRouter

router = APIRouter(
    tags='Goods',
    prefix=['/goods']
)



@router.get('/goods')
async def get_goods():
    ...