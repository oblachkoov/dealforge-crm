from src.backend.domain.shared.errors import DomainError


class LeadError(DomainError):
    """
    Базовая ошибка Lead
    """

class FieldTypeNotSelect(LeadError):
    """
    Вызывается когда тип пользовательского поля не вызван
    """

class EnumValueAlreadyExistsError(LeadError):
    """
    Вызывается когда значение enum уже существует
    """

class InvalidEnumValue(LeadError):
    """
    Вызывается когда enum невалидный
    """