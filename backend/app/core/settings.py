from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = "DOJO_MANAGER ERP"
    VERSION: str = "0.9.5"

    DATABASE_URL: str = (
        "postgresql+psycopg://"
        "postgres:postgres@localhost:5432/dojo_manager"
    )

    ENVIRONMENT: str = "development"


    class Config:
        env_file = ".env"


@lru_cache
def get_settings():

    return Settings()