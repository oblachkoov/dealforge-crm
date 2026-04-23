from dataclasses import dataclass

from backend.src.backend.application.funnel.dtos.list_funnel import ListFunnelCommand
from backend.src.backend.application.shared.dtos.paginaton import PageResult
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.funnel.entity import Funnel
from backend.src.backend.domain.user.entity import User


@dataclass
class ListFunnelUseCase:
    uow: UnitOfWork
    user: User

    async def execute(
            self,
            cmd: ListFunnelCommand
    ) -> PageResult[Funnel]:
        async with self.uow:
            result = await self.uow.funnels.get_funnels(cmd)
            return result
