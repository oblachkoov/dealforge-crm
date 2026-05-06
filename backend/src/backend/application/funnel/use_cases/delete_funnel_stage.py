from dataclasses import dataclass

from backend.src.backend.application.funnel.services.stage_ordering import FunnelStageOrderingService
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.funnel.entity import Funnel, FunnelStage
from backend.src.backend.domain.funnel.policies.can_delete import CanDeleteFunnelPolicy
from backend.src.backend.domain.user.entity import User


@dataclass
class DeleteFunnelStageUseCase:
    uow: UnitOfWork
    funnel: Funnel
    stage: FunnelStage
    ordering: FunnelStageOrderingService
    user: User

    async def execute(self):
        CanDeleteFunnelPolicy(self.user).enforce()

        async with self.uow:
            stages = await self.uow.stages.get_funnel_stages(self.funnel.id)
            updated = self.ordering.remove(stages, self.stage)

            await self.uow.stages.delete_funnel_stage(self.stage)
            await self.uow.stages.save_all(updated)
            await self.uow.commit()
