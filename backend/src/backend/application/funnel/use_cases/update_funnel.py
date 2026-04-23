from dataclasses import dataclass

from backend.src.backend.application.funnel.dtos.update_funnel import UpdateFunnelCommand
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.funnel.entity import Funnel
from backend.src.backend.domain.funnel.policies.can_update import CanUpdateFunnelPolicy
from backend.src.backend.domain.user.entity import User


@dataclass
class UpdateFunnelUseCase:
    uow: UnitOfWork
    user: User
    funnel: Funnel

    async def execute(
            self,
            cmd: UpdateFunnelCommand
    ) -> None:
        CanUpdateFunnelPolicy(self.user).enforce()
        async with self.uow:
            self.funnel.change_name(cmd.name)
            await self.uow.funnels.update_funnel(self.funnel)
            await self.uow.commit()