from idlelib.rpc import response_queue

from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from starlette import status

from backend.src.backend.application.auth.dtos.change_password import ChangePasswordCommand
from backend.src.backend.application.auth.dtos.get_me import GetMeResult
from backend.src.backend.application.auth.dtos.login_user import LoginUserCommand, LoginUserResult
from backend.src.backend.application.auth.dtos.refresh_token import RefreshTokenCommand, RefreshTokenResult
from backend.src.backend.application.auth.dtos.update_me import UpdateMeCommand
from backend.src.backend.application.auth.use_cases.change_password import ChangePasswordUseCase
from backend.src.backend.application.auth.use_cases.login_user import LoginUserUseCase
from backend.src.backend.application.auth.use_cases.refresh_token import RefreshTokenUseCase
from backend.src.backend.application.auth.use_cases.update_me import UpdateMeUseCase
from backend.src.backend.domain.shared.specification import Specification
from backend.src.backend.domain.user.entity import User
from backend.src.backend.domain.user.specifications.password import PasswordDifferenceSpecification
from backend.src.backend.infrastracture.db.sqlalchemy.core.uow import SqlAlchemyUnitOfWork
from backend.src.backend.infrastracture.security.argon2.hasher import Argon2Hasher
from backend.src.backend.infrastracture.security.jose.token import JWTTokenService
from backend.src.backend.presentation.api.v1.auth.dependencies import get_hasher, get_token_service, get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@cbv(router)
class AuthRouter:
    uow: SqlAlchemyUnitOfWork = Depends()

    @router.post(
        "/login",
        name="Авторизация",
        status_code=status.HTTP_201_CREATED,
        response_model=LoginUserResult
    )
    async def login(
            self,
            request: LoginUserCommand,
            hasher: Argon2Hasher = Depends(get_hasher),
            tokens: JWTTokenService = Depends(get_token_service)
    ):
        uc = LoginUserUseCase(
            uow=self.uow,
            tokens=tokens,
            hasher=hasher,
        )
        response = await uc.execute(
            cmd=request
        )
        return response

    @router.post(
        "/refresh",
        name="Обновление Токена",
        status_code=status.HTTP_201_CREATED,
        response_model=RefreshTokenResult,
    )
    async def refresh(
        self,
        request: RefreshTokenCommand,
        tokens: JWTTokenService = Depends(get_token_service)
    ):
        uc = RefreshTokenUseCase(
            uow=self.uow,
            tokens=tokens,
        )
        response = await uc.execute(
            cmd=request
        )
        return response

    @router.get(
        "/me",
        name="Получение персональной информации",
        status_code=status.HTTP_200_OK,
        response_model=GetMeResult
    )
    async def get_me(
            self,
            user: User = Depends(get_current_user),
    ):
        return user

    @router.post(
        "/change-password",
        name="Изменение пароля",
        status_code=status.HTTP_201_CREATED,
    )
    async def change_password(
            self,
            request: ChangePasswordCommand,
            user: User = Depends(get_current_user),
            hasher: Argon2Hasher = Depends(get_hasher),
            password_spec: Specification[str] = Depends(get_password_spec),
            password_diff_spec: PasswordDifferenceSpecification = Depends(get_password_diff_spec)
    ):
        uc = ChangePasswordUseCase(
            uow=self.uow,
            hasher=hasher,
            password_spec=password_spec,
            password_diff_spec=password_diff_spec,
            user=user
        )
        response = await uc.execute(
            cmd=request
        )
        return response


    @router.patch(
        "/me",
        name="Обновление персональной информации",
        status_code=status.HTTP_201_CREATED,
    )
    async def update_me(
            self,
            request: UpdateMeCommand,
            user: User = Depends(get_current_user),
    ):
        uc = UpdateMeUseCase(
            uow=self.uow,
            user=user
        )
        response = await uc.execute(
            cmd=request
        )
        return response
