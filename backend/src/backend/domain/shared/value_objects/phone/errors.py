from src.backend.domain.shared.errors import DomainError


class PhoneError(DomainError):
    """
    Базовая ошибка VO Phone
    """

class InvalidPhoneFormatError(PhoneError):
    """
    Вызывается когда указали неправильный формат номера телефона
    """
