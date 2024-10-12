from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    # is_active: Optional[bool] = True
    # full_name: Optional[str] = None
    # password: str
    # hashed_password: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    email: EmailStr
    password: str
    # user_name: Optional[str] = None
