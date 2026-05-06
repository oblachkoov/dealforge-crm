from dataclasses import dataclass

from tomlkit.source import Source

from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.user.entity import User


@dataclass
class RegenerateWebhookSecretUseCase:
    uow: UnitOfWork
    user: User
    source: Source

    async def execute(self):
        if self.source.source_type != SourceType.webhook:
            raise NotWebhookSourceError()
        token = self.source.regenerate_secret()
        async with self.uow:
            await self.uow.sources.update(self.source)
            await self.uow.commit()
        return token
