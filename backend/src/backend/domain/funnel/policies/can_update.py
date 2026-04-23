from backend.src.backend.domain.shared.policy import Policy
from backend.src.backend.domain.user.entity import UserRole, User


class CanUpdateFunnelPolicy(Policy):
    ALLOWED_ROLES = {UserRole.admin, UserRole.director}

    def __init__(self, actor: User):
        self._actor = actor

    def is_satisfied_by(self) -> bool:
        return self._actor.role in self.ALLOWED_ROLES


    def _error_message(self) -> str:
        return f"You can't update funnel"