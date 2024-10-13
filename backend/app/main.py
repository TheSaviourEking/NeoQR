from fastapi import FastAPI

# from app import models, db
from app.db.base import Base
from app.models import user, qrcode
from app.api.v1.router import router as v1_router

# from app.db.base import Base
from app.db.session import engine


app = FastAPI()
# Base.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)


# models.Base.metadata.create_all(db.base.engine)
# db.base.Base.metadata.create_all(db.base.engine)

app.include_router(v1_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "NeoQR API is online"}
