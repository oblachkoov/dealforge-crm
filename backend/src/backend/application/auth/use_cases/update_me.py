from dataclasses import dataclass

from backend.src.backend.application.auth.dtos.update_me import UpdateMeCommand
from backend.src.backend.application.auth.errors import EmailAlreadyExistsError
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.user.entity import User


@dataclass
class UpdateMeUseCase:
    uow: UnitOfWork
    user: User

    async def execute(
            self,
            cmd: UpdateMeCommand
    ):
        async with self.uow:
            exists = await self.uow.users.exists_email(str(cmd.email), self.user.id)

            if exists:
                raise EmailAlreadyExistsError()

            self.user.change_first_name(cmd.first_name)
            self.user.change_last_name(cmd.last_name)
            self.user.change_email(str(cmd.email))

            await self.uow.users.update(self.user)
            await self.uow.commit()