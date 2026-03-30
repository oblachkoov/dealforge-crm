from backend.domain.shared.errors import DomainError


class NameError(DomainError):
    """
    Базовая ошибка VO Name
    """


class NameTypeError(NameError):
    """
    Вызывается когда указан неправильный тип значения
    """


class InvalidNameLengthError(NameError):
    """
    Вызывается когда длина имени вне допустимого диапазона
    """


class InvalidNameFormatError(NameError):
    """
    Вызывается когда формат имени неправильный
    """