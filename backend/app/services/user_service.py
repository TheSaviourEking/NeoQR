from sqlalchemy.orm import Session
from ..schemas.user import UserCreate, UserAuth
from app.models.user import User
from app.core.security import get_password_hash, create_access_token

from app.crud.users import user
from fastapi import HTTPException, status


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user_data: UserCreate):
        existing_user = user.get(self.db, field="email", value=user_data.email)

        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_password = get_password_hash(user_data.password)

        new_user = User(
            email=user_data.email,
            hashed_password=hashed_password,
            firstname=user_data.firstname,
            lastname=user_data.lastname,
        )

        new_user = user.create(self.db, new_user)
        return new_user

    def login_user(self, user_data: UserAuth):
        login_user = user.authenticate_user(
            self.db, email=user_data.email, password=user_data.password
        )

        if not login_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )

        else:
            # Create JWT token
            access_token = create_access_token(data={"sub": login_user.email})
            return {"access_token": access_token, "token_type": "Bearer"}
