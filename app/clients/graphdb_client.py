import requests
from app.config.settings import settings

class GraphDBClient:
    def run_query(self, query: str):
        response = requests.post(
            settings.GRAPHDB_REPO_URL,
            data={"query": query},
            headers={"Accept": "application/sparql+json"},
            timeout=10
        )
        response.raise_for_status()
        return response.json()