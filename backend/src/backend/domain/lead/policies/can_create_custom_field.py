from backend.src.backend.domain.shared.policy import Policy
from backend.src.backend.domain.user.entity import UserRole, User


class CanCreateCustomFieldPolicy(Policy):
    """
    Определяет, может ли пользователь создать пользовательское поле
    """
    ALLOWED_ROLES = {UserRole.admin, UserRole.director}

    def __init__(self, actor: User):
        """
        Attributes::
             actor: пользователь, который выполняет действие
        """

        self._actor = actor

    def is_satisfied_by(self) -> bool:
        """
        Определяет, может ли пользователь создать пользовательское поле

        Returns:
            True если может
        """

        return self._actor.role in self.ALLOWED_ROLES


    def _error_message(self) -> str:
        """
        Возвращает сообщение об ошибке

        Returns:
            строку с описанием
        """
        return f"You can't create custom field"
