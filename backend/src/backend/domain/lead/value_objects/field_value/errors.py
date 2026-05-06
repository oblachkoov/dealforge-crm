from backend.src.backend.domain.shared.errors import DomainError


class FieldValueError(DomainError):
    """
    Базовая ошибка VO FieldValue
    """

class EmptyFieldValueError(FieldValueError):
    """
    Вызывается когда ни одно поле не заполнено
    """


class MultipleFieldValueError(FieldValueError):
    """
    Вызывается когда заполнено больше одного поля
    """