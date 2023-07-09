from passlib.context import CryptContext
from pydantic import EmailStr
from app.users.dao import UserDAO

password_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_user(plain_password, verify_password) -> bool:
    return password_context.verify(plain_password, verify_password)


async def authentificate_user(email: EmailStr, password):
    user = await UserDAO.find_one_or_none(email=email)
    if not user and not verify_user(password, user.password):
        return None
    return user
