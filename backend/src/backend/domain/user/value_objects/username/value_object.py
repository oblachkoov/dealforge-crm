import re
from dataclasses import dataclass

from backend.src.backend.domain.user.value_objects.username.errors import UnSupportedUsernameTypeError, \
    InvalidUsernameLengthError, InvalidUsernameFormatError


@dataclass(frozen=True)
class Username:
    """
    Vo Username
    """
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise UnSupportedUsernameTypeError()

        if len(self.value) <=3 or len(self.value) > 255:
            raise InvalidUsernameLengthError()

        if not self.__is_valid():
            raise InvalidUsernameFormatError()

        object.__setattr__(self,'value', self.value.lower())

    def __is_valid(self) -> bool:
        """
        Приватная функция для проверки валидного username
        :return: True или False
        """
        pattern = r'^[a-zA-Z][a-zA-Z0-9_]*$'
        return re.match(pattern, self.value) is not None

