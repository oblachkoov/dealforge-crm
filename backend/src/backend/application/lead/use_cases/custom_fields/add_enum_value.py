from dataclasses import dataclass

from backend.src.backend.application.lead.dtos.custom_fields.add_enum_value import AddEnumValueCommand
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.lead.entity import LeadCustomField
from backend.src.backend.domain.lead.policies.can_add_enum_value import CanAddEnumValuePolicy
from backend.src.backend.domain.user.entity import User


@dataclass
class AddEnumValueUseCase:
    uow: UnitOfWork
    user: User
    custom_field: LeadCustomField

    async def execute(
            self,
            cmd: AddEnumValueCommand
    ) -> None:
        CanAddEnumValuePolicy(self.user).enforce()
        async with self.uow:
            self.custom_field.add_enum(cmd.value)
            await self.uow.custom_fields.update(self.custom_field)
            await self.uow.commit()