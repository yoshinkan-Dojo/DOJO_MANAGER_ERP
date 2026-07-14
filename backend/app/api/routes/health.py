from fastapi import APIRouter


router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "online",
        "project": "DOJO_MANAGER ERP",
        "version": "0.9.5"
    }