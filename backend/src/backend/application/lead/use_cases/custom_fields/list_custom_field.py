from dataclasses import dataclass

from src.backend.application.shared.interfaces.uow import UnitOfWork
from src.backend.domain.lead.entity import LeadCustomField
from src.backend.domain.user.entity import User


@dataclass
class ListCustomFieldUseCase:
    uow: UnitOfWork

    async def execute(self) -> list[LeadCustomField]:
        async with self.uow:
            fields = await self.uow.custom_fields.list()
            return fields