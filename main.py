from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.types import Lifespan

from src.apps import routers
from src.common.events import close_clients, create_clients
from src.config.settings import settings


def get_app(_lifespan: Lifespan | None = None) -> FastAPI:
    _app = FastAPI(
        title="TRR Foundational Service",
        version="0.1.0",
        description="TRR Foundational Service API using RDF and GraphDB",
        lifespan=_lifespan,
    )
    _app.include_router(routers.api_router, prefix="/api/v1")
    return _app


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    await create_clients(app)
    yield
    await close_clients(app)


app = get_app(_lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True,
    )
