from pydantic import BaseModel


class ImpactResponse(BaseModel):
    regulatory_update: str
    tax_rule: str


class ImpactListResponse(BaseModel):
    data: list[ImpactResponse]
    total_count: int
