import pytest

from backend.domain.shared.value_objects.email.errors import InvalidEmailError
from backend.domain.shared.value_objects.email.value_objects import Email


import pytest

from backend.src.backend.domain.shared.value_objects.email.value_objects import Email


@pytest.fixture
def test_email():
    return Email("testuser@gmail.com")



@pytest.mark.parametrize(
    "value", "expected",
    [
        ("user1.test@gmail.com", "user1.test@gmail.com"),
        ("alex_smith23@yahoo.com", "alex_smith23@yahoo.com"),
        ("maria.dev2024@outlook.com", "maria.dev2024@outlook.com"),
        ("john.doe.dev@mail.com", "john.doe.dev@mail.com"),
        ("test.user001@gmail.com", "test.user001@gmail.com"),
        ("backend.fastapi@proton.me", "backend.fastapi@proton.me"),
        ("demo.account99@yahoo.com", "demo.account99@yahoo.com"),
        ("frontend.dev123@gmail.com", "frontend.dev123@gmail.com"),
        ("example.user777@outlook.com", "example.user777@outlook.com"),
        ("visola.project@mail.com", "visola.project@mail.com")
    ]
)
def test_valid_email(value, expected):
    assert Email(value).value == expected



@pytest.mark.parametrize(
    "value",
    [
        "usergmail.com"
        "@gmail.com"
        "user@"
        "user@.com"
        "user@com"
        "user@@gmail.com"
        "user gmail@gmail.com"
        "user#gmail.com"
        "user@gmail..com"
        "user@-gmail.com"
    ]
)
def test_invalid_email(value):
    with pytest.raises(InvalidEmailError):
        Email(value)