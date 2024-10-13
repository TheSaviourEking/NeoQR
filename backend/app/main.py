import asyncio

from fastapi import FastAPI

# from app import models, db
from app.db.base import Base
from app.api.v1.router import router as v1_router

# from app.db.base import Base
from app.db.session import engine
from app.api.dependencies import init_db


app = FastAPI()
# Base.metadata.create_all(engine)


@app.on_event("startup")
async def on_startup():
    await init_db()
    # pass
    # Base.metadata.create_all(engine)


app.include_router(v1_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "NeoQR API is online"}


if __name__ == "__main__":
    import uvicorn

    asyncio.run(init_db())
    uvicorn.run(app, host="0.0.0.0", port=8000)
