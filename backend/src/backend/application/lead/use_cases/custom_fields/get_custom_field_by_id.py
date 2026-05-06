from dataclasses import dataclass

from backend.src.backend.application.lead.dtos.custom_fields.get_custom_field_by_id import GetCustomFieldByIdCommand
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork


@dataclass
class GetCustomFieldByIdUseCase:
    uow: UnitOfWork

    async def execute(
            self,
            cmd: GetCustomFieldByIdCommand
    ):
        async with self.uow:
            field = await self.uow.custom_fields.get_by_id(cmd.id)
            if not field:
                raise
            return field