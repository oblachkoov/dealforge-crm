from dataclasses import dataclass, replace

from ansible_collections.google.cloud.plugins.modules.gcp_cloudbuild_trigger import WebhookConfig
from tomlkit.source import Source

from backend.src.backend.application.shared.interfaces.uow import UnitOfWork
from backend.src.backend.domain.user.entity import User


@dataclass
class UpdateSourceUseCase:
    uow: UnitOfWork
    user: User
    source: Source

    async def execute(
            self,
            cmd
    ) -> None:
        # Policy
        async with self.uow:
            self.source.change_name(cmd.name)
        if cmd.config.type != self.source_type:
            raise
        new_config = await self.build_update_config(self.source, cmd.config)
        if new_config is not None:
            self.source.change_config(new_config)
        await self.uow.sources.update(self.source)
        await self.uow.commit()
    async def build_update_config(
            self,
            source: Source,
            patch: UpdateSourceConfigDTO
    )-> SourceConfig | None:
        match patch:
            case UpdateWebhookConfigDTO():
                pass

    async def _update_webhook_config(
            self,
            current: WebhookConfig,
            patch: UpdateWebhookConfigDTo
    ) -> WebhookConfig:
        changes = patch.model_dump(execute_unset=True, exclude={"type"})

        if not changes:
            return current

        new_funnel_id = changes.get("default_funnel_id", current.default_funnel_id)
        new_stage_id = changes.get("default_stage_id", current.default_stage_id)

        if "default_funnel_id" in changes or "default_stage_id" in changes:
            await self._ensure_assignment_pool(changes["assignment_pool"])

        if "assignment_pool" in changes:
            changes["assignment_pool"] = tuple(changes["assignment_pool"])

        return replace(current, **changes)

    async def _update_public_form(
            self,
            source: Source,
            patch: UpdatePublicFormConfigDTO
    ):
        pass