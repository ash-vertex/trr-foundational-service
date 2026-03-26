from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1 import health, impact
from app.db.session import close_db_engines, create_db_engines


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_engines(app)
    yield
    await close_db_engines(app)


app = FastAPI(
    title="TRR Foundational Service",
    version="0.1.0",
    description="TRR Foundational Service API using RDF and GraphDB",
    lifespan=lifespan,
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(impact.router, prefix="/api/v1")