from dataclasses import dataclass

from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.application.user.dtos.delete_user import DeleteUserCommand
from backend.src.backend.application.user.errors import UserNotFoundError
from backend.src.backend.domain.user.entity import User
from backend.src.backend.domain.user.policies.can_delete import CanDeleteUserPolicy


@dataclass
class DeleteUserUseCase:
    uow: UnitOfWork
    actor: User

    async def execute(
            self,
            user_id: DeleteUserCommand
    ):
        async with self.uow:
            user = await self.uow.users.get_by_id(user_id.id)
            if not user:
                raise UserNotFoundError()

            CanDeleteUserPolicy(self.actor, user.role).enforce()

            await self.uow.users.delete(user)
            await self.uow.commit()


