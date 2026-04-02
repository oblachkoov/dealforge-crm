import pytest

from tests.unit.domain.shared.value_objects.username.errors import UnSupportedUsernameTypeError, \
    InvalidUsernameLengthError, InvalidUsernameFormatError
from tests.unit.domain.shared.value_objects.username.value_objects import Username

@pytest.fixture
def test_name():
    return Username("")

@pytest.mark.parametrize(
    "value", "expected",
    [
        ("user123", "user123"),
        ("alex_dev", "alex_dev"),
        ("boburbek", "boburbek"),
        ("python_senior", "python_senior"),
        ("admin_99", "admin_99"),
        ("my_super_login", "my_super_login"),
        ("uzb_developer", "uzb_developer"),
        ("test_user_account", "test_user_account"),
        ("it_specialist", "it_specialist"),
        ("fastapi_master", "fastapi_master")
    ]

)
def test_valid_username(value, expected):
    assert Username(value).value == expected



@pytest.mark.parametrize(
    "value",
    [
        1,
        [1, 2, 3],
        True,
        1.6
    ]
)

def test_unsupprted_type_username(value):
    with pytest.raises(UnSupportedUsernameTypeError):
        Username(value)


@pytest.mark.parametrize(
    "value",
    [
        "aa",
        "a1",
        "a",
        "a"*256,
        "python_developer"*100
    ]
)
def test_invalid_username_length(value):
    with pytest.raises(InvalidUsernameLengthError):
        Username(value)


@pytest.mark.parametrize(
    "value",
    [
        "1username",
        "_user123",
        "777python",
        "user.name",
        "alex-dev",
        "hello world",
        "user@name",
        "admin!",
        "dev#ops",
        "бобурбек",
        "user_тест",
        "my-name-123",
        "user/name",
        "active.user",
        "double__underscore"
    ]
)
def test_valid_username_format(value):
    with pytest.raises(InvalidUsernameFormatError):
        Username(value)