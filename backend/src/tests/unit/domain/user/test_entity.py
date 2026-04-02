from ast import Name
from datetime import datetime

import pytest
import uuid

from backend.src.backend.domain.shared.errors import DomainError
from backend.src.backend.domain.shared.value_objects.email.value_objects import Email
from backend.src.tests.unit.domain.shared.value_objects.username.value_objects import Username
from backend.src.tests.unit.domain.user.entity import User
from backend.src.tests.unit.domain.user.value_objects import test_username
from backend.src.tests.unit.domain.user.value_objects.test_username import test_name
from backend.src.tests.unit.domain.value_objects.test_email import test_email


@pytest.fixture
def user_id() -> uuid.UUID:
    return uuid.uuid4()

@pytest.fixture
def password_hash() -> str:
    return "hashed_password"


@pytest.fixture
def valid_user() -> User:
    return User(
        id=user_id,
        first_name=test_name,
        last_name=test_name,
        email=test_email,
        username=test_username,
        password_hash=password_hash,
    )

def test_create_user(user_id: uuid.UUID) -> None:
    user = User.create(
        id=user_id,
        first_name=test_name.value,
        last_name=test_name.value,
        email=test_email.value,
        username=test_username.value,
        password_hash=password_hash,
    )
    assert user.id == user_id
    assert user.first_name == test_name
    assert user.last_name == test_name
    assert user.email == test_email
    assert user.username == test_username
    assert user.password_hash == password_hash


@pytest.mark.parametrize(
    "first_name,last_name,email,username",
    [
        ("a", "Test", "testuser@gmail.com", "testuser"),
        ("Test", "a", "testuser@gmail.com", "testuser"),
        ("testuser@gmail.com", "Test", "a", "testuser"),
        ("testuser@gmail.com", "testuser", "a", "Test"),
    ]
)
def test_invalid_create_user(
        first_name,
        last_name,
        email,
        username,
        password_hash,
):
    with pytest.raises(DomainError):
        User.create(
            id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password_hash=password_hash
        )

def test_user_full_name(valid_user):
    full_name = f"{valid_user.first_name} {valid_user.last_name}"
    assert valid_user.full_name == full_name


def test_user_touch(valid_user):
    before_update = valid_user.updated_at
    valid_user.touch()
    assert valid_user.updated_at > before_update


def test_user_interact(valid_user):
    valid_user.last_interact()
    assert isinstance(valid_user.last_interaction, datetime.datetime)


