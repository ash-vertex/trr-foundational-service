from fastapi import APIRouter

from src.apps.db.api import db_router
from src.apps.health.api import health_router
from src.apps.impact.api import impact_router

api_router = APIRouter()

api_router.include_router(health_router, prefix="/health", tags=["Health"])
api_router.include_router(impact_router, prefix="/impact", tags=["Impact"])
api_router.include_router(db_router, prefix="/db", tags=["DB Connection Test"])
