from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from starlette import status

from backend.src.backend.application.user.dtos.create_user import CreateUserResult, CreateUserCommand
from backend.src.backend.application.user.use_cases.create_user import CreateUserUseCase
from backend.src.backend.domain.shared.specification import Specification
from backend.src.backend.domain.user.entity import User
from backend.src.backend.infrastracture.db.sqlalchemy.core.uow import SqlAlchemyUnitOfWork
from backend.src.backend.infrastracture.security.argon2.hasher import Argon2Hasher
from backend.src.backend.presentation.api.v1.auth.dependencies import get_current_user, get_hasher, get_password_spec

router= APIRouter(
    prefix="/users",
    tags=["user"]
)

@cbv(router)
class UserRouter:
    uow: SqlAlchemyUnitOfWork = Depends(get_current_user)
    user: User = Depends(get_current_user)

    @router.post(
        "/",
        name="Создание пользователя",
        status_code=status.HTTP_201_CREATED,
        response_model=CreateUserResult,
    )
    async def create_user(
            self,
            request: CreateUserCommand,
            hasher: Argon2Hasher = Depends(get_hasher),
            password_spec: Specification[str] = Depends(get_password_spec),
    ):
        uc = CreateUserUseCase(
            uow=self.uow,
            hasher=hasher,
            password_spec=password_spec,
            actor=self.user
        )
        response = await uc.execute(
            cmd=request
        )
        return response

