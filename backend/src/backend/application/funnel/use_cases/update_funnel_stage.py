from dataclasses import dataclass

from backend.src.backend.application.funnel.dtos.update_funnel_stage import UpdateFunnelStageCommand
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.funnel.entity import Funnel, FunnelStage
from backend.src.backend.domain.funnel.policies.can_update import CanUpdateFunnelPolicy
from backend.src.backend.domain.user.entity import User


@dataclass
class UpdateFunnelStageUseCase:
    uow: UnitOfWork
    funnel: Funnel
    stage: FunnelStage
    user: User

    async def execute(
            self,
            cmd: UpdateFunnelStageCommand
    ):
        CanUpdateFunnelPolicy(self.user).enforce()
        async with self.uow:
            self.stage.change(
                name=cmd.name,
                win_probability=cmd.win_probability,
                hex=cmd.hex
            )
            await self.uow.stages.update_funnel_stage(self.stage)
            await self.uow.commit()