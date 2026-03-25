from app.clients.graphdb_client import GraphDBClient
from app.sparql.impact_queries import IMPACT_BY_JURISDICTION
from app.models.impact_models import ImpactResponse

class ImpactService:
    def __init__(self):
        self.graphdb = GraphDBClient()

    def get_impacts_by_jurisdiction(self, jurisdiction: str):
        query = IMPACT_BY_JURISDICTION.format(jurisdiction=jurisdiction)
        result = self.graphdb.run_query(query)

        response = []
        for row in result["results"]["bindings"]:
            response.append(
                ImpactResponse(
                    regulatory_update=row["update"]["value"],
                    tax_rule=row["rule"]["value"]
                )
            )

        return response