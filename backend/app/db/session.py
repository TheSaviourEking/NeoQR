from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

connect_args = {"check_same_thread": False}
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, connect_args=connect_args, echo=True
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    autocommit=False,
    expire_on_commit=False,
    autoflush=False,
    # class_=AsyncSession
)


class _AsyncSessionContextManager:
    def __init__(self, connection):
        self.connection = connection

    async def __aenter__(self):
        self.session = AsyncSession(self.connection)
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
