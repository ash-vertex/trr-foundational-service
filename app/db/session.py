from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from fastapi import FastAPI

from app.config.settings import settings


def create_db_engines(app: FastAPI) -> None:
    grip_engine = create_async_engine(settings.GRIP_DB_URL, pool_pre_ping=True, echo=False)
    vcms_engine = create_async_engine(settings.VCMS_DB_URL, pool_pre_ping=True, echo=False)

    app.state.grip_engine = grip_engine
    app.state.vcms_engine = vcms_engine

    app.state.GripSession = async_sessionmaker(bind=grip_engine, expire_on_commit=False)
    app.state.VcmsSession = async_sessionmaker(bind=vcms_engine, expire_on_commit=False)


async def close_db_engines(app: FastAPI) -> None:
    await app.state.grip_engine.dispose()
    await app.state.vcms_engine.dispose()
