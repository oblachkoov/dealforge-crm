from dataclasses import dataclass, field
from enum import StrEnum
from uuid import UUID

from backend.src.backend.domain.funnel.value_objects.probability.value_object import Probability
from backend.src.backend.domain.shared.entity import BaseEntity
from backend.src.backend.domain.shared.mixins import TimeActionMixin
from backend.src.backend.domain.shared.value_objects.hex.value_object import HexCode
from backend.src.backend.domain.shared.value_objects.name.value_object import Name


@dataclass
class Funnel(BaseEntity, TimeActionMixin):
    """
    Главная сущность воронка продаж

    Attributes:
        id: уникальный идентификатор
        name: название
        is_deleted: удален или нет
        created_at: временная метка создания
        updated_at: временная метка обновления
    """
    name: Name
    is_deleted: bool = field(default=False)

    @classmethod
    def create(
        cls,
        name:str
    ):
        """
        Создает объект воронки

        Args:
            name: название

        Returns:
            Объект воронки продаж
        """
        return cls(
            name=Name(name)
        )

    def change_name(self, name: str):
        """
        Изменяет имя название воронки

        Attributes:
            name: название
        """
        self.name = Name(name)
        self.touch()

    def delete(self):
        """
        Меняет значение поля is_deleted на True
        """
        self.is_deleted = True
        self.touch()

    def restore(self):
        """
        Меняет значение поля is_deleted на False
        """
        self.is_deleted = False
        self.touch()



class StageKind(StrEnum):
    initial = "initial"
    intermediate = "intermediate"
    won = "won"
    lost = "lost"

@dataclass
class FunnelStage(BaseEntity, TimeActionMixin):
    """
    Сущность этапа воронки

    Attributes:
        id: уникальный идентификатор
        funnel_id: ид воронки продаж
        name: название
        win_probability: вероятность успеха
        hex_code: код hex
        order: порядок
        created_at: временная метка создания
        updated_at: временная метка обновления
    """
    funnel_id: UUID
    name: Name
    win_probability: Probability
    hex_code: HexCode = field(default_factory=lambda: HexCode("#B255D4"))
    order: int = field(default=0)
    is_archived: bool = field(default=False)
    kind: StageKind = field(default=StageKind.initial)

    @classmethod
    def create(
        cls,
        funnel_id: UUID,
        name: str,
        win_probability: int,
        hex_code: str,
        order: int = 0,
    ):
        """
       Создает объект этапа воронки

       Args:
            funnel_id: ид воронки продаж
            name: название
            win_probability: вероятность успеха
            hex_code: код hex
            order: порядок

       Returns:
           Объект этапа воронки
       """
        return cls(
            funnel_id=funnel_id,
            name=Name(name),
            win_probability=Probability(win_probability),
            hex_code=HexCode(hex_code),
            order=order
        )

    def change_order(self, order: int):
        """
        Изменяет порядок этапа

        Attributes:
            order: порядок
        """
        self.order = order
        self.touch()

    def change(
            self,
            name: str,
            win_probability: int,
            hex_code: str,
    ):
        """
        Изменяет этап воронки

        Attributes:
            name: название
            win_probability: вероятность успеха
            hex_code: код hex
        """
        self.name = Name(name)
        self.win_probability = Probability(win_probability)
        self.hex_code = HexCode(hex_code)
        self.touch()
