from typing import Protocol
from uuid import UUID

from backend.src.backend.application.funnel.dtos.list_funnel import ListFunnelCommand
from backend.src.backend.application.shared.dtos.paginaton import PageResult
from backend.src.backend.domain.funnel.entity import Funnel


class FunnelRepository(Protocol):
    async def create_funnel(self, funnel: Funnel) -> Funnel: ...

    async def update_funnel(self, funnel: Funnel) -> Funnel: ...

    async def delete_funnel(self, funnel: Funnel) -> None: ...

    async def get_funnel_by_id_funnel(self, funnel_id: UUID) -> Funnel | None: ...

    async def get_funnels(self, cmd: ListFunnelCommand) -> PageResult[Funnel]: ...