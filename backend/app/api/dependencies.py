from app.db.session import AsyncSessionLocal, engine
from fastapi import HTTPException, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession
from jose import JWTError, jwt
from app.crud.users import user as user_crud
from app.core import security, config

from app.db import base, session

# Dependency injection function for FastAPI
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


async def init_db():
    async with session.engine.begin() as conn:
        # await conn.run_sync(base.Base.metadata.drop_all)
        await conn.run_sync(base.Base.metadata.create_all)


async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            # await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()


# To BE USED IN PROTECTED ROUTES
async def get_current_user(
    token: str = Depends(security.oauth2_scheme), db: AsyncSession = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token, config.settings.SECRET_KEY, algorithms=[config.settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = security.TokenData(username=email)

    except JWTError:
        raise credentials_exception

    user = user_crud.get(db, field="email", value=token_data.username)
    if user is None:
        raise credentials_exception
    return user
