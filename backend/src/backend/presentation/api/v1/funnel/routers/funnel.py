from fastapi import APIRouter, Depends, Query
from fastapi_utils.cbv import cbv
from starlette import status

from backend.src.backend.application.funnel.dtos.create_funnel import CreateFunnelResult, CreateFunnelCommand
from backend.src.backend.application.funnel.dtos.list_funnel import ListFunnelCommand
from backend.src.backend.application.funnel.dtos.update_funnel import UpdateFunnelCommand
from backend.src.backend.application.funnel.use_cases.create_funnel import CreateFunnelUseCase
from backend.src.backend.application.funnel.use_cases.delete_funnel import DeleteFunnelUseCase
from backend.src.backend.application.funnel.use_cases.list_funnel import ListFunnelUseCase
from backend.src.backend.application.funnel.use_cases.update_funnel import UpdateFunnelUseCase
from backend.src.backend.application.shared.dtos.paginaton import PageRequest
from backend.src.backend.domain.funnel.entity import Funnel
from backend.src.backend.domain.user.entity import User
from backend.src.backend.infrastracture.db.sqlalchemy.core.uow import SqlAlchemyUnitOfWork
from backend.src.backend.presentation.api.v1.auth.dependencies import get_current_user
from backend.src.backend.presentation.api.v1.core.dependencies import get_uow
from backend.src.backend.presentation.api.v1.funnel.dependencies import get_funnel

router= APIRouter(
    prefix="/funnels",
    tags=["funnel"]
)

@cbv(router)
class FunnelRouter:
    uow: SqlAlchemyUnitOfWork = Depends(get_uow)
    user: User = Depends(get_current_user)

    @router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
        response_model=CreateFunnelResult,
    )
    async def create_funnel(
            self,
            request: CreateFunnelCommand
    ):
        uc = CreateFunnelUseCase(
            uow=self.uow,
            user=self.user
        )
        response = await uc.execute(
            cmd=request
        )
        return response

    @router.get(
        "/{funnel_id}",
        status_code=status.HTTP_200_OK,
        response_model=Funnel
    )
    async def get_funnel(
            self,
            funnel: Funnel = Depends(get_funnel)
    ):
        return funnel


    @router.get(
        "/",
        status_code=status.HTTP_200_OK,
    )
    async def list_funnels(
            self,
            q: str | None = Query(default=None),
            sort_by: str | None = Query(default=None),
            page: int = Query(default=1),
            size: int = Query(default=100)
    ):
        request = ListFunnelCommand(q=q, sort_by=sort_by, pagination=PageRequest(page=page, size=size))
        uc = ListFunnelUseCase(
            uow=self.uow,
            user=self.user
        )
        response = await uc.execute(
            cmd=request
        )
        return response


    @router.patch(
        "/{funnel_id}",
        status_code=status.HTTP_200_OK,
    )
    async def update_funnel(
            self,
            request: UpdateFunnelCommand,
            funnel: Funnel = Depends(get_funnel),
    ):
        uc = UpdateFunnelUseCase(
            uow=self.uow,
            user=self.user,
            funnel=funnel
        )
        response = await uc.execute(
            cmd=request
        )
        return response

    @router.delete(
        "/{funnel_id}",
        status_code=status.HTTP_200_OK,
    )
    async def delete_funnel(
            self,
            funnel: Funnel = Depends(get_funnel),
    ):
        uc = DeleteFunnelUseCase(
            uow=self.uow,
            user=self.user,
            funnel=funnel
        )
        response = await uc.execute()
        return response