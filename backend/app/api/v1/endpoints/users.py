from fastapi import APIRouter

from app.schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.post("/", response_model=UserResponse)
async def create_user(user_data: UserCreate):
    # Logic to create a user
    # Call controller
    # return {"message": "User created", "user": user_data}
    return {"message": "User created", "user": user_data}


@router.get("/{user_id}")
async def get_user(user_id: int):
    # Logic to get a user by ID
    return {"user_id": user_id, "name": "John Doe"}
