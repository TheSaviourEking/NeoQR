from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserAuth
from app.schemas.profile import ProfileCreate
from app.models.user import User, Profile
from app.core.security import get_password_hash, create_access_token

# from sqlalchemy.orm import Session

from app.crud import users, profile as profile_crud
from fastapi import HTTPException, status


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_data: UserCreate):
        # async with self.db() as session:
        existing_user = await users.user.get(
            self.db, field="email", value=user_data.email
        )

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = get_password_hash(user_data.password)

        new_user = User(
            email=user_data.email,
            hashed_password=hashed_password,
            firstname=user_data.firstname,
            lastname=user_data.lastname,
        )

        # new_user = await users.user.create(self.db, new_user)
        new_user = await users.user.create(self.db, new_user)

        profile_service = ProfileService(self.db)
        await profile_service.create_profile(new_user.id, user_data.profile)

        return new_user

    async def login_user(self, user_data: UserAuth):
        login_user = users.user.authenticate_user(
            self.db, email=user_data.email, password=user_data.password
        )

        if not login_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Create JWT token
        access_token = create_access_token(data={"sub": login_user.id})
        return {"access_token": access_token, "token_type": "Bearer"}


class ProfileService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_profile(self, user_id: int, profile_data: ProfileCreate):

        new_profile = Profile(
            bio=profile_data.bio,
            profile_image=profile_data.profile_image,
            website=profile_data.website,
            location=profile_data.location,
            user_id=user_id,
        )

        # print(profile_data, "eee")
        new_profile = await profile_crud.profile.create(self.db, new_profile)

        # self.db.add(new_profile)
        # self.db.commit()
        # self.db.refresh(new_profile)
        return new_profile
        # return ProfileCreate.parse_obj(profile_data)
