from dataclasses import dataclass

from src.backend.application.lead.dtos.custom_fields.rename_custom_field import RenameCustomFieldCommand
from src.backend.application.shared.interfaces.uow import UnitOfWork
from src.backend.domain.lead.entity import LeadCustomField
from src.backend.domain.lead.policies.can_rename__custom_field import CanRenameCustomFieldPolicy
from src.backend.domain.user.entity import User


@dataclass
class RenameCustomFieldUseCase:
    uow: UnitOfWork
    user: User
    custom_field: LeadCustomField

    async def execute(
            self,
            cmd: RenameCustomFieldCommand
    ):
        CanRenameCustomFieldPolicy(self.user).enforce()
        async with self.uow:
            self.custom_field.rename(cmd.name)
            await self.uow.custom_fields.update(self.custom_field)
            await self.uow.commit()
