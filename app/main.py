from fastapi import FastAPI
from app.api.v1 import health,impact
app = FastAPI(
	title="TRR Foundational Service",
	version="0.1.0",
	description="TRR Foundational Service API using RDF and GraphDB"
)
app.include_router(health.router, prefix="/api/v1")
app.include_router(impact.router, prefix="/api/v1")