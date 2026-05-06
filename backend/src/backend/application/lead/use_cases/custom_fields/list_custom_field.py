from dataclasses import dataclass

from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.lead.entity import LeadCustomField



@dataclass
class ListCustomFieldUseCase:
    uow: UnitOfWork

    async def execute(self) -> list[LeadCustomField]:
        async with self.uow:
            fields = await self.uow.custom_fields.list()
            return fields