from dataclasses import dataclass

from backend.src.backend.application.shared.dtos.paginaton import PageResult
from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.application.user.dtos.get_source import GetSourceResult
from backend.src.backend.application.user.dtos.list_source import ListSourceCommand
from backend.src.backend.domain.user.entity import User


@dataclass
class ListSourceUseCase:
    uow: UnitOfWork
    user: User

    async def execute(
            self,
            cmd: ListSourceCommand
    ) -> PageResult[GetSourceResult]:
        async with self.uow:
            sources = await self.uow.sources.list(cmd)

            return PageResult[GetSourceResult](
                items=[
                    to_result(source)
                    for source in sources
                ],
                page=sources.page,
                size=sources.size,
                total_items=sources.total_items
            )