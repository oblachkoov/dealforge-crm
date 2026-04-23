from uuid import UUID

from fastapi import Depends

from backend.src.backend.application.funnel.dtos.get_funnel import GetFunnelCommand
from backend.src.backend.application.funnel.use_cases.get_funnel import GetFunnelUseCase
from backend.src.backend.domain.user.entity import User
from backend.src.backend.infrastracture.db.sqlalchemy.core.uow import SqlAlchemyUnitOfWork
from backend.src.backend.presentation.api.v1.auth.dependencies import get_current_user


async def get_funnel(
        funnel_id: UUID,
        user: User = Depends(get_current_user),
        uow: SqlAlchemyUnitOfWork = Depends(get_uow)
):
    uc = GetFunnelUseCase(
        uow=uow,
        user=user
    )
    funnel = await uc.execute(GetFunnelCommand(funnel_id=funnel_id))
    return funnel