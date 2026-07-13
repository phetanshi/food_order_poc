from fastapi import APIRouter

health_router = APIRouter(
    prefix="/api/health",
    tags=["Health"],
)


@health_router.get("")
async def health():
    return {
        "status": "Healthy",
        "database": "Connected",
        "application": "Nahansh Food Ordering AI",
    }