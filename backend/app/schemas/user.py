from pydantic import BaseModel, EmailStr
from typing import Optional
from .profile import ProfileCreate


class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    # hashed_password: str

    # is_active: Optional[bool] = True
    # full_name: Optional[str] = None
    # password: str
    # hashed_password: str


class UserCreate(UserBase):
    password: str
    profile: ProfileCreate


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True


class UserAuth(BaseModel):
    email: EmailStr
    password: str
    # user_name: Optional[str] = None
