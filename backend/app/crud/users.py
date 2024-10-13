from app.models.user import User
from app.crud.base import CRUDBase
from sqlalchemy.orm import Session
from typing import Optional
from app.core.security import verify_password
from app.schemas.user import UserCreate, UserUpdate

# user = CRUDBase(User)


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def __init__(self, model: User):
        super().__init__(model)

    def authenticate_user(
        self, db: Session, email: str, password: str
    ) -> Optional[User]:
        user = db.query(self.model).filter(self.model.email == email).first()

        if user and verify_password(password, user.hashed_password):
            return user
        # return login_user
        # user = user.get(self.db, field="email", value=user_data.email)

        # Check if user exists and validate password
        # if not user or not verify_password(user_login.password, user.hashed_password):
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="Invalid credentials",
        #         headers={"WWW-Authenticate": "Bearer"},
        #     )

        return None


user = CRUDUser(User)
