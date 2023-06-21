from fastapi import FastAPI
from app.goods.router import router as goods_router


app = FastAPI(title='Stock')

app.include_router(goods_router)


@app.get('/')
def home():
    return 'hollow at Stock'