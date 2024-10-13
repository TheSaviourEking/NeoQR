from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    DATABASE_URL: str

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "NeoQR"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

        env_required = ["DATABASE_URL", "SECRET_KEY"]


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
