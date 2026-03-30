from backend.domain.shared.errors import DomainError


class IdError(DomainError):
    """
    Это Базовая ошибка VO Id
    """

class UnsupportedTypeIdError(IdError):
    """
    Вызывается когда дают не подлежающий тип значения
    """

class NegativeIntIdError(IdError):
    """
    Вызывается когда дают отрицательно значение
    """