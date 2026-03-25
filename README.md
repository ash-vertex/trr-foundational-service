# TRR Foundational Service

Project structure and setup instructions.


## RDF Functionality PoC

This section demonstrates how to test the core RDF functionality in this project, including generating RDF data and querying it via the API.

### 1. Generate RDF Data

Use the ETL script to convert your data to RDF (Turtle format):

```bash
python etl/to_rdf.py
```

This will create or update RDF files in the `rdf/` directory.

### 2. Start the API Server

Run the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at: http://localhost:8001

### 3. Test RDF Query Endpoint

You can test the RDF query endpoint (example):

```bash
curl -X POST "http://localhost:8000/api/v1/impact/query" \
	-H "Content-Type: application/json" \
	-d '{"query": "SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 10"}'
```

Replace the query as needed for your use case.

---
For more details, see the code in `app/clients/graphdb_client.py`, `app/sparql/impact_queries.py`, and `app/utils/sparql_utils.py`.
