from dataclasses import dataclass

from backend.src.backend.domain.shared.mixins import IDMixin

@dataclass
class BaseEntity(IDMixin):
    """
    Базовая сущность

    Attributes:
        id: Уникальный идентификатор
    """

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other: "BaseEntity"):
        return self.id == other.id

