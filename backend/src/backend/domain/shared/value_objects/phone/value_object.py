import re
from dataclasses import dataclass

from backend.src.backend.domain.shared.value_objects.phone.errors import InvalidPhoneFormatError


@dataclass(frozen=True)
class Phone:
    """
    VO Phone

    Attributes:
        value: Значение в типе данных str
    """
    value: str

    def __post_init__(self):
        if not self.__is_valid():
            raise InvalidPhoneFormatError()

    def __is_valid(self) -> bool:
        """
        Приватная функция для проверки валидного номера телефона

        Returns:
             True если формат правильный
        """
        # Очищаем строку от пробелов, скобок и тире
        clean_phone = re.sub(r'[\s\(\)\-]', '', self.value)

        # Регулярное выражение:
        # ^\+          - начинается с плюса
        # [1-9]        - первая цифра кода страны (не ноль)
        # \d{1,3}      - еще до 3-х цифр кода страны
        # \d{5,12}     - от 5 до 12 цифр самого номера
        # $            - конец строки
        pattern = r'^\+[1-9]\d{1,3}\d{5,12}$'

        return bool(re.match(pattern, clean_phone))
