from dataclasses import dataclass

from backend.src.backend.application.auth.dtos.get_me import GetMeCommand
from backend.src.backend.application.auth.errors import InActiveUserError
from backend.src.backend.application.auth.interfaces.security.token import TokenService
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.user.entity import User


@dataclass
class GetMeUseCase:
    uow: UnitOfWork
    tokens: TokenService

    async def execute(
            self,
            cmd: GetMeCommand
    ) -> User:
        async with self.uow:
            user_id = self.tokens.decode(cmd.token)

            user = await self.uow.users.get_by_id(user_id)

            if not user:
                raise InActiveUserError()

            # return GetMeResult(
            #     id=user.id,
            #     first_name=user.first_name.value,
            #     last_name=user.last_name.value,
            #     username=user.username.value,
            #     email=user.email.value,
            #     is_active=user.is_active,
            #     last_interaction=user.last_interaction,
            # )
            return user

