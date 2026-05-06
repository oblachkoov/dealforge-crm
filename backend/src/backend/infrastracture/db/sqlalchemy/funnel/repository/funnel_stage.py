from uuid import UUID

from sqlalchemy import select, delete

from backend.src.backend.application.funnel.repository import FunnelStageRepository
from backend.src.backend.domain.funnel.entity import FunnelStage, StageKind
from backend.src.backend.domain.funnel.value_objects.probability.value_object import Probability
from backend.src.backend.domain.shared.value_objects.hex.value_object import HexCode
from backend.src.backend.domain.shared.value_objects.name.value_object import Name
from backend.src.backend.infrastracture.db.sqlalchemy.core.repository import SqlAlchemyRepository
from backend.src.backend.infrastracture.db.sqlalchemy.funnel.models import FunnelStageModel


def to_model(stage: FunnelStage) -> FunnelStageModel:
    return FunnelStageModel(
        id=stage.id,
        funnel_id=stage.funnel_id,
        name=str(stage.name),
        win_probability=int(stage.win_probability),
        hex=str(stage.hex_code),
        order=stage.order,
        is_archived=stage.is_archived,
        kind=stage.kind,
        created_at=stage.created_at,
        updated_at=stage.updated_at,
    )


def to_entity(stage: FunnelStageModel) -> FunnelStage:
    return FunnelStage(
        id=stage.id,
        funnel_id=stage.funnel_id,
        name=Name(stage.name),
        win_probability=Probability(stage.win_probability),
        hex_code=HexCode(stage.hex),
        order=stage.order,
        is_archived=stage.is_archived,
        kind=StageKind(stage.kind),
        created_at=stage.created_at,
        updated_at=stage.updated_at,
    )

class SqlAlchemyFunnelStageRepository(SqlAlchemyRepository, FunnelStageRepository):
    async def get_funnel_stage_by_id(self, stage_id: UUID) -> FunnelStage:
        stmt = select(FunnelStageModel).where(FunnelStageModel.id == stage_id)
        result = await self.session.execute(stmt)
        stage = result.scalar_one_or_none()
        return to_entity(stage) if stage else None

    async def update_funnel_stage(self, stage: FunnelStage) -> FunnelStage:
        instance = to_model(stage)
        await self.session.merge(instance)
        await self.session.flush()
        return to_entity(instance)

    async def delete_funnel_stage(self, stage: FunnelStage) -> None:
        # instance = to_model(stage)
        # await self.session.delete(instance)
        # await self.session.flush()

        stmt = delete(FunnelStageModel).where(FunnelStageModel.id == stage.id)
        await self.session.execute(stmt)
        await self.session.flush()

    async def save_all(self, stages: list[FunnelStage]) -> None:
        for s in stages:
            instance = to_model(s)
            await self.session.merge(instance)
        await self.session.flush()

    async def get_funnel_stages(self, funnel_id: UUID) -> list[FunnelStage]:
        stmt = select(FunnelStageModel).where(FunnelStageModel.funnel_id == funnel_id)
        result = await self.session.execute(stmt)
        stages = result.scalars().all()
        return [to_entity(s) for s in stages]
