from fastapi import APIRouter
from app.users.dao import UserDAO
from app.users.schemas import SUserAuth, SUserReg
from app.exeptions import UserAlreadyExistExeption
from app.users.auth import get_hashed_password, authentificate_user


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
async def auth(user: SUserAuth):
    return await authentificate_user(user.email, user.password)
