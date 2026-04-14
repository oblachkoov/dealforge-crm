from ast import Name

import pytest

from backend.src.backend.domain.shared.value_objects.name.errors import InvalidNameLengthError, InvalidNameFormatError


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Alex", "Alex"),
        ("John", "John"),
        ("Michael", "Michael"),
        ("Anna", "Anna"),
        ("David", "David"),
        ("Sofia", "Sofia"),
        ("Daniel", "Daniel"),
        ("Robert", "Robert"),
        ("Emily", "Emily"),
        ("James", "James")
    ]
)
def test_valid_name(value, expected):
    assert Name(value).value == expected


@pytest.mark.parametrize(
    "value",
    [
        1,
        [1, 2, 3],
        True,
        1.6
    ]
)
def test_type_name(value):
    with pytest.raises(NameTypeError):
        Name(value)


@pytest.mark.parametrize(
    "value",
    [
        "A",
        "B",
        "C",
        "a" * 101,
        "verylongname" * 20
    ]
)
def test_invalid_name_length(value):
    with pytest.raises(InvalidNameLengthError):
        Name(value)


@pytest.mark.parametrize(
    "value",
    [
        "alex123",
        "john_doe",
        "anna@name",
        "mike!",
        "hello world",
        "name#test",
        "123name",
        "_alex",
        "alex_",
        "alex--dev",
        "alex.dev",
        "бобурбек",
        "anna maria1",
        "name/name"
    ]
)
def test_invalid_name_format(value):
    with pytest.raises(InvalidNameFormatError):
        Name(value)