from dataclasses import dataclass

from backend.src.backend.application.auth.dtos.change_password import ChangePasswordCommand
from backend.src.backend.application.auth.errors import WeakPasswordError, SamePasswordError, AuthUserNotFoundError, \
    InvalidPasswordError
from backend.src.backend.application.auth.interfaces.security.hasher import Hasher
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.shared.specification import Specification


@dataclass
class ChangePasswordUseCase:
    uow: UnitOfWork
    hasher: Hasher
    password_spec: Specification[str]
    password_diff_spec: Specification[tuple[str, str]]

    async def execute(self, cmd: ChangePasswordCommand):
        if not self.password_spec.is_satisfied_by(cmd.new_password):
            raise WeakPasswordError()

        if not self.password_diff_spec.is_satisfied_by((cmd.old_password, cmd.new_password)):
            raise SamePasswordError()

        async with self.uow as uow:
            user = await uow.users.get_by_id(cmd.user_id)

            if not user:
                raise AuthUserNotFoundError()

            if not self.hasher.verify(cmd.old_password, user.password_hash):
                raise InvalidPasswordError()

            user.change_password(self.hasher.hash(cmd.new_password))
            await self.uow.users.update(user)
            await uow.commit()

