from pydantic import BaseModel

class ImpactResponse(BaseModel):
    regulatory_update: str
    tax_rule: str