from fastapi import APIRouter, Depends, status

from src.apps.impact import serializers
from src.apps.impact.dependencies import get_impact_service
from src.apps.impact.service import ImpactService

impact_router = APIRouter()


@impact_router.get(
    "/jurisdiction/{jurisdiction}",
    status_code=status.HTTP_200_OK,
    name="Get Impacts by Jurisdiction",
    response_model=list[serializers.ImpactResponse],
)
def get_impacts_by_jurisdiction(
    jurisdiction: str,
    impact_service: ImpactService = Depends(get_impact_service),  # noqa: B008
) -> list[serializers.ImpactResponse]:
    return impact_service.get_impacts_by_jurisdiction(jurisdiction=jurisdiction)
