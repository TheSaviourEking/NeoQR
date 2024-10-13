from fastapi import APIRouter, Depends
from app.schemas.user import UserAuth, UserCreate
from app.services.user_service import UserService

from sqlalchemy.ext.asyncio import AsyncSession
from app.api.dependencies import get_db
from app.core.security import Token

router = APIRouter()


# LOGIN
@router.post("/login", response_model=Token)
async def login(user_data: UserAuth, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)

    logged_in_user = user_service.login_user(user_data)
    return logged_in_user


@router.post("/signup")
async def signup(user_details: UserCreate, db: AsyncSession = Depends(get_db)):
    user_service = UserService(db)

    created_user = await user_service.create_user(user_data=user_details)

    return created_user
