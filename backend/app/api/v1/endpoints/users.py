from fastapi import APIRouter

router = APIRouter()

@router.post("/users/")
async def create_user(user_data: dict):
    # Logic to create a user
    return {"message": "User created", "user": user_data}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    # Logic to get a user by ID
    return {"user_id": user_id, "name": "John Doe"}
