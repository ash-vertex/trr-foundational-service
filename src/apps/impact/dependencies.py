from fastapi import Depends

from src.apps.impact.service import ImpactService
from src.common.events import GraphDBClient, get_graphdb_client


def get_impact_service(
    graphdb: GraphDBClient = Depends(get_graphdb_client),  # noqa: B008
) -> ImpactService:
    return ImpactService(graphdb=graphdb)
