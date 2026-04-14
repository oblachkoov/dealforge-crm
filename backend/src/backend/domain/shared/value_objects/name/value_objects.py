import re
from dataclasses import dataclass


from backend.src.backend.domain.shared.value_objects.name.errors import InvalidNameLengthError, InvalidNameFormatError
from backend.src.backend.domain.user.value_objects.username.errors import UnSupportedUsernameTypeError


@dataclass(frozen=True)
class Name:
    """
    VO Name
    """
    value: str

    def __post_init__(self):
        #Проверка типа данных
        if not isinstance(self.value, str):
            raise UnSupportedUsernameTypeError()

        #Проверка длины
        if len(self.value) < 2 or len(self.value) > 255:
            raise InvalidNameLengthError

        #Проверка формата
        if not self.__is_valid():
            raise InvalidNameFormatError


        object.__setattr__(self, 'value', self.value)


    def __is_valid(self):
        pattern = r'^[a-zA-Z][a-zA-Z0-9_]*$'
        return re.match(pattern, self.value) is not None