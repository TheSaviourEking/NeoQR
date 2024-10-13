from fastapi import APIRouter, Depends
from app.schemas.user import UserAuth
from app.services.user_service import UserService
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.schemas.user import UserCreate

router = APIRouter()


# LOGIN
@router.post("/login")
async def login(user_data: UserAuth, db: Session = Depends(get_db)):
    user_service = UserService(db)

    logged_in_user = user_service.login_user(user_data)
    return logged_in_user


@router.post("/signup")
def signup(user_details: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)

    created_user = user_service.create_user(user_data=user_details)

    return created_user
