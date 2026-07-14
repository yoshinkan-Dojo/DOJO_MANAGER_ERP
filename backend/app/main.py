from fastapi import FastAPI

from app.api.routes.health import router as health_router


app = FastAPI(
    title="DOJO_MANAGER ERP",
    version="0.9.5",
    description="ERP especializado para escolas de artes marciais",
)


app.include_router(
    health_router
)