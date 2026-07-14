from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.settings import get_settings


settings = get_settings()


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)


app.include_router(
    health_router
)