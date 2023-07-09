from fastapi import APIRouter, Response
from app.users.dao import UserDAO
from app.users.schemas import SUserAuth, SUserReg
from app.exeptions import UserAlreadyExistExeption
from app.users.auth import get_hashed_password, authentificate_user, create_access_token


router = APIRouter(
    prefix='/users',
    tags=['User and auth']
)


@router.post('/signup')
async def create_user(user: SUserReg):
    existing_user = await UserDAO.find_one_or_none(email=user.email)
    if existing_user:
        raise UserAlreadyExistExeption
    user.hashed_password = get_hashed_password(user.hashed_password)
    await UserDAO.add(dict(user))


@router.post('/signin')
async def auth(user_data: SUserAuth, response: Response):
    user = await authentificate_user(user_data.email, user_data.password)
    if not user:
        return 'Invalid user or pass'
    access_token = create_access_token({'sub': str(user.id)})
    response.set_cookie('stock_access_token', access_token, httponly=True)
    return access_token
