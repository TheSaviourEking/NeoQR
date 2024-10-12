from fastapi import FastAPI

from app.api.v1.router import router as api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "NeoQR API is online"}
