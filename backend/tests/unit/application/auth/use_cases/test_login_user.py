import pytest

from backend.src.backend.application.auth.dtos.login_user import LoginUserCommand
from backend.src.backend.application.auth.errors import AuthUserNotFoundError, InvalidPasswordError, InActiveUserError
from backend.src.backend.application.auth.use_cases.login_user import LoginUserUseCase
from backend.src.backend.domain.user.entity import User
from backend.tests.unit.application.auth.interfaces.security.fake_hasher import FakeHasher
from backend.tests.unit.application.auth.interfaces.security.fake_token import FakeTokenService
from backend.tests.unit.application.shared.interfaces.fake_uow import FakeUnitOfWork


@pytest.fixture()
def login_user_command() -> LoginUserCommand:
    return LoginUserCommand(
        username="username",
        password="password"
    )

def make_use_case(user: User=None, password_match: bool = True) -> LoginUserUseCase:
    return LoginUserUseCase(
        uow=FakeUnitOfWork(user=user),
        tokens=FakeTokenService(),
        hasher=FakeHasher(result=password_match)
    )

@pytest.mark.asyncio
async def test_successful_login_user(login_user_command: LoginUserCommand, valid_user: User):
    use_case = make_use_case(user=valid_user)
    result = await use_case.execute(login_user_command)
    assert result.access_token == f"token: {valid_user.id}"
    assert result.refresh_token == f"token: {valid_user.id}"
    assert result.token_type == "Bearer"


@pytest.mark.asyncio
async def test_login_user_not_found(login_user_command: LoginUserCommand):
    use_case = make_use_case(user=None)

    with pytest.raises(AuthUserNotFoundError):
        await use_case.execute(login_user_command)


@pytest.mark.asyncio
async def test_login_user_invalid_password(login_user_command: LoginUserCommand, valid_user: User):
    use_case = make_use_case(user=valid_user, password_match=False)

    with pytest.raises(InvalidPasswordError):
        await use_case.execute(login_user_command)


@pytest.mark.asyncio
async def test_login_user_inactive_user(login_user_command: LoginUserCommand, valid_user: User):
    valid_user.is_active = False
    use_case = make_use_case(user=valid_user)

    with pytest.raises(InActiveUserError):
        await use_case.execute(login_user_command)