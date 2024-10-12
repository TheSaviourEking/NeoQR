from fastapi import APIRouter

from app.api.v1.endpoints import users, items, auth

router = APIRouter()

router.include_router(auth.router, prefix="/users", tags=["users"])
router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(items.router, prefix="/items", tags=["items"])
