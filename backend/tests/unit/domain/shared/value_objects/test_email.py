import pytest

from backend.src.backend.domain.shared.value_objects.email.errors import InvalidEmailError
from backend.src.backend.domain.shared.value_objects.email.value_object import Email


@pytest.fixture
def test_email():
    return Email("testuser@gmail.com")

@pytest.mark.parametrize(
    "value, expected",
    [
        ("alpha.user@gmail.com", "alpha.user@gmail.com"),
        ("coolguy123@yahoo.com", "coolguy123@yahoo.com"),
        ("name_test@outlook.com", "name_test@outlook.com"),
        ("email-test@mail.ru", "email-test@mail.ru"),
        ("hello.dev@company.org", "hello.dev@company.org"),
        ("user2026@test.net", "user2026@test.net"),
        ("first_name@domain.co", "first_name@domain.co"),
        ("simpleuser@mail.com", "simpleuser@mail.com"),
        ("coder.girl123@service.io", "coder.girl123@service.io"),
        ("abc_xyz@sub.domain.com", "abc_xyz@sub.domain.com"),
    ]
)
def test_valid_email(value, expected):
    assert Email(value).value == expected


@pytest.mark.parametrize(
    "value",
    [
        "plainaddress",  # нет @
        "@no-local-part.com",  # нет имени до @
        "user@",  # нет домена
        "user@.com",  # домен начинается с точки
        "user@com",  # нет точки в домене
        "user@domain..com",  # двойная точка
        "user@@domain.com",  # два @
        "user domain@domain.com",  # пробел внутри
        "user#domain.com",  # нет @ вообще
        "user@domain,com"  # запятая вместо точки
    ]
)
def test_invalid_email(value):
    with pytest.raises(InvalidEmailError):
        Email(value)