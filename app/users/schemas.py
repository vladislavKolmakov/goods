from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserReg(BaseModel):
    username: str
    name: str
    second_name: str
    surname: str
    hashed_password: str
    email: EmailStr

    class Config:
        orm_mode = True
