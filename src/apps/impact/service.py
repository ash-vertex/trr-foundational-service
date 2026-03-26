from src.apps.impact import serializers
from src.apps.impact.sparql.queries import IMPACT_BY_JURISDICTION
from src.common.events import GraphDBClient


class ImpactService:
    def __init__(self, graphdb: GraphDBClient) -> None:
        self.graphdb = graphdb

    def get_impacts_by_jurisdiction(self, jurisdiction: str) -> list[serializers.ImpactResponse]:
        query = IMPACT_BY_JURISDICTION.format(jurisdiction=jurisdiction)
        result = self.graphdb.run_query(query)

        return [
            serializers.ImpactResponse(
                regulatory_update=row["update"]["value"],
                tax_rule=row["rule"]["value"],
            )
            for row in result["results"]["bindings"]
        ]
