from dataclasses import dataclass

from backend.src.backend.application.lead.dtos.custom_fields.remove_enum_value import RemoveEnumValueCommand
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.lead.entity import LeadCustomField
from backend.src.backend.domain.lead.policies.can_remove_enum_value import CanRemoveEnumValuePolicy
from backend.src.backend.domain.user.entity import User


@dataclass
class RemoveEnumValueUseCase:
    uow: UnitOfWork
    user: User
    custom_field: LeadCustomField

    async def execute(
            self,
            cmd: RemoveEnumValueCommand
    ) -> None:
        CanRemoveEnumValuePolicy(self.user).enforce()
        async with self.uow:
            self.custom_field.remove_enum(cmd.enum_id)
            await self.uow.custom_fields.update(self.custom_field)
            await self.uow.commit()