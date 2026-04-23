from enum import StrEnum

from pydantic import BaseModel

from backend.src.backend.application.shared.dtos.paginaton import PageRequest


class FunnelSortEnum(StrEnum):
    name_asc = "name:asc"
    name_desc = "name:desc"
    created_at_asc = "created_at:asc"
    created_at_desc = "created_at:desc"

class ListFunnelCommand(BaseModel):
    q: str | None = None
    sort_by: str | None = None
    pagination: PageRequest


