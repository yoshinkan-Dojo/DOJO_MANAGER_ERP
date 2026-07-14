from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "DOJO_MANAGER ERP"
    VERSION: str = "0.9.5"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str
    SQLALCHEMY_ECHO: bool = False

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()
