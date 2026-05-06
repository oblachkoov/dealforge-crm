from backend.src.backend.domain.shared.errors import DomainError


class LeadNameVOError(DomainError):
    """
    Базовая ошибка VO LeadName
    """

class UnSupportedLeadNameTypeError(LeadNameVOError):
    """
    Вызывается когда указали неправильный тип значения
    """

class InvalidLeadNameLengthError(LeadNameVOError):
    """
    Вызывается когда длина имени превышает диапазон
    """

