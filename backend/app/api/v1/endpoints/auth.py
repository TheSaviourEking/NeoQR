from fastapi import APIRouter
from app.schemas.user import UserAuth

router = APIRouter()


# LOGIN
@router.post("/login")
async def login(user_data: UserAuth):
    return {"message": "here"}


@router.get("/signup")
def signup():
    """heoooo"""
    return "here"
