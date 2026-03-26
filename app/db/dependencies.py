from collections.abc import AsyncGenerator

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.datastructures import State


async def get_state(request: Request) -> State:
    return request.app.state


async def get_grip_db(state: State = Depends(get_state)) -> AsyncGenerator[AsyncSession, None]:
    async with state.GripSession() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise


async def get_vcms_db(state: State = Depends(get_state)) -> AsyncGenerator[AsyncSession, None]:
    async with state.VcmsSession() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
