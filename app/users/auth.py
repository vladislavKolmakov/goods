from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from pydantic import EmailStr
from app.users.dao import UserDAO
from app.config import ALGORITHM

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_user(plain_password, verify_password) -> bool:
    return password_context.verify(plain_password, verify_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode, "secret_key", algorithm="HS256"
        # to_encode, SECRET_KEY, ALGORITHM
    )
    return encoded_jwt


async def authentificate_user(email: EmailStr, password):
    user = await UserDAO.find_one_or_none(email=email)
    if not user and not verify_user(password, user.password):
        return None
    return user
