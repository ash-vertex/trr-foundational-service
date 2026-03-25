from fastapi import APIRouter
from app.services.impact_service import ImpactService
from app.models.impact_models import ImpactResponse
router = APIRouter(prefix="/impact", tags=["Impact"])
service = ImpactService()

@router.get("/jurisdiction/{jurisdiction}", response_model=list[ImpactResponse])
def impact_by_jurisdiction(jurisdiction: str):
    return service.get_impacts_by_jurisdiction(jurisdiction)