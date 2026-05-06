from dataclasses import dataclass

from tomlkit.source import Source

from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.application.user.dtos.get_source import GetSourceResponse, GetSourceCommand, GetSourceResult
from backend.src.backend.domain.user.entity import User


@dataclass
class GetSourceUseCase:
    uow: UnitOfWork
    user: User
    public_base_url: str = ""

    async def execute(
        self,
        cmd: GetSourceCommand
    )-> GetSourceResult:
        async with self.ouw:
            source = await self.uow.sources.get_by_id(cmd.source_id)
            if not source or source.is_deleted:
                raise
            return self._to_result(source)

    def _to_result(self, source: Source) -> GetSourceResult:
        return GetSourceResult(
            id=source.id,
            name=source.name,
            type=source.type,
            config=self._config_to_view(source.config),
            is_deleted=source.is_deleted,
            is_active=source.is_active,
            created_at=source.created_at,
            updated_at=source.updated_at,
        )
