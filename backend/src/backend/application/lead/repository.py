from typing import Protocol
from uuid import UUID

from src.backend.domain.lead.entity import LeadCustomField


class LeadCustomFieldRepository(Protocol):
    async def add(self, field: LeadCustomField) -> LeadCustomField: ...

    async def update(self, field: LeadCustomField) -> None: ...

    async def get_by_id(self, field_id: UUID) -> LeadCustomField | None: ...

    async def list(self) -> list[LeadCustomField]: ...