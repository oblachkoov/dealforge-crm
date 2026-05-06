from dataclasses import dataclass

from tomlkit.source import Source

from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.user.entity import User


@dataclass
class ActivateSourceUseCase:
    uow: UnitOfWork
    user: User
    source: Source

    async def execute(self):
        async with self.uow:
            self.source.activate()
            await self.uow.sources.update(self.source)
            await self.uow.commit()

