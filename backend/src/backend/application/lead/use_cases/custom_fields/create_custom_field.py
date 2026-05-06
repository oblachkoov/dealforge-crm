from dataclasses import dataclass

from backend.src.backend.application.lead.dtos.custom_fields.create_customa_fields import CreateCustomFieldCommand
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.lead.entity import LeadCustomField
from backend.src.backend.domain.lead.policies.can_create_custom_field import CanCreateCustomFieldPolicy
from backend.src.backend.domain.user.entity import User


@dataclass
class CreateCustomFieldUseCase:
    uow: UnitOfWork
    user: User

    async def execute(
            self,
            cmd: CreateCustomFieldCommand
    ):
        CanCreateCustomFieldPolicy(self.user).enforce()
        async with self.uow:
            field = LeadCustomField.create(
                name=cmd.name,
                type=cmd.type
            )

            if cmd.type.is_select:
                if not cmd.enums_values:
                    raise

                for v in cmd.enums_values:
                    field.add_enum(v)

            await self.uow.custom_fields.add(field)
            await self.uow.commit()
            return