from collections.abc import AsyncGenerator

import requests
from fastapi import Depends, FastAPI, Request
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from starlette.datastructures import State

from src.config.settings import settings


# --- Lifespan events ---

async def create_clients(app: FastAPI) -> None:
    grip_engine = create_async_engine(settings.GRIP_DB_URL, pool_pre_ping=True, echo=False)

    vcms_connect_args = {}
    if settings.VCMS_DB_SSL:
        vcms_connect_args["sslmode"] = "require"

    vcms_engine = create_async_engine(
        settings.VCMS_DB_URL,
        pool_pre_ping=True,
        echo=False,
        connect_args=vcms_connect_args,
    )

    app.state.grip_engine = grip_engine
    app.state.vcms_engine = vcms_engine
    app.state.GripSession = async_sessionmaker(bind=grip_engine, expire_on_commit=False)
    app.state.VcmsSession = async_sessionmaker(bind=vcms_engine, expire_on_commit=False)

    app.state.graphdb_url = settings.GRAPHDB_REPO_URL


async def close_clients(app: FastAPI) -> None:
    await app.state.grip_engine.dispose()
    await app.state.vcms_engine.dispose()


# --- DB session dependencies ---

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


# --- GraphDB client ---

class GraphDBClient:
    def __init__(self, repo_url: str) -> None:
        self._repo_url = repo_url

    def run_query(self, query: str) -> dict:
        response = requests.post(
            self._repo_url,
            data={"query": query},
            headers={
                "Accept": "application/sparql-results+json",
                "Content-Type": "application/x-www-form-urlencoded",
            },
            timeout=10,
        )
        response.raise_for_status()
        return response.json()


async def get_graphdb_client(state: State = Depends(get_state)) -> GraphDBClient:
    return GraphDBClient(repo_url=state.graphdb_url)
