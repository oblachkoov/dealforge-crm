from dataclasses import dataclass

from src.backend.application.shared.interfaces.uow import UnitOfWork
from src.backend.domain.lead.entity import LeadCustomField
from src.backend.domain.lead.policies.can_delete_custom_field import CanDeleteCustomFieldPolicy
from src.backend.domain.user.entity import User


@dataclass
class DeleteCustomFieldUseCase:
    uow: UnitOfWork
    user: User
    custom_field: LeadCustomField

    async def execute(
            self,
    ):
        CanDeleteCustomFieldPolicy(self.user).enforce()
        async with self.uow:
            self.custom_field.delete()
            await self.uow.custom_fields.update(self.custom_field)
            await self.uow.commit()
