from fastapi import APIRouter, status

health_router = APIRouter()


@health_router.get("", status_code=status.HTTP_200_OK, name="Health Check")
async def health_check() -> dict:
    return {"status": "UP"}
