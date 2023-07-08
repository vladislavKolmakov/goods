from fastapi import FastAPI
from app.goods.router import router as goods_router
from app.users.router import router as users_router


app = FastAPI(title='Stock')

app.include_router(goods_router)
app.include_router(users_router)


@app.get('/')
def home():
    return 'hollow at Stock'