import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Email:
    """
    VO Email нужен для полей в котороых будет электронная почта

    Attributes:
        value (str): Значение в типе данных str
    """
    value: int


    def __post_init__(self):
        if not self.__is_valid():
            raise

    def __is_valid(self)-> bool:
        """
        Приватная Функция для проверки  валидного email
        :return:
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
        return re.match(pattern, self.value) is not None
