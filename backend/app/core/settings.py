from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "DOJO_MANAGER ERP"
    VERSION: str = "0.9.5"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str
    SQLALCHEMY_ECHO: bool = False
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
