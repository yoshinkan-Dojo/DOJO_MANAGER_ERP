from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.auth.routes import router as auth_router
from app.users.routes import router as users_router


app = FastAPI(
    title="DOJO_MANAGER ERP",
    version="0.9.5",
    description="ERP especializado para escolas de artes marciais",
)


app.include_router(
    health_router
)
app.include_router(auth_router)
app.include_router(users_router)
