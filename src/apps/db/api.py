from fastapi import APIRouter, Depends, status
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.common.events import get_grip_db, get_vcms_db

db_router = APIRouter()


@db_router.get(
    "/grip/ping",
    status_code=status.HTTP_200_OK,
    name="Test GRIP DB Connection",
)
async def ping_grip_db(
    db: AsyncSession = Depends(get_grip_db),  # noqa: B008
) -> dict:
    result = await db.execute(text("SELECT 1"))
    value = result.scalar()
    return {"database": "grip", "status": "connected", "result": value}


@db_router.get(
    "/vcms/ping",
    status_code=status.HTTP_200_OK,
    name="Test VCMS DB Connection",
)
async def ping_vcms_db(
    db: AsyncSession = Depends(get_vcms_db),  # noqa: B008
) -> dict:
    result = await db.execute(text("SELECT 1"))
    value = result.scalar()
    return {"database": "vcms", "status": "connected", "result": value}
