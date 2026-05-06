from dataclasses import dataclass
from datetime import date
from uuid import UUID

from src.backend.domain.lead.value_objects.field_value.errors import EmptyFieldValueError, MultipleFieldValueError


@dataclass(frozen=True)
class FieldValue:
    """
    VO Field

    Attributes:
        value_text: текстовое значение
        value_number: числовое значение
        value_boolean: логическое значение
        value_date: значение даты
        enum_id: ид enum
    """
    value_text: str | None = None
    value_number: int | None = None
    value_boolean: bool | None = None
    value_date: date | None = None
    enum_id: UUID | None = None

    def __post_init__(self):
        fields = [self.value_text, self.value_number, self.value_boolean, self.value_date, self.enum_id]
        field_count = sum(1 for f in fields if f is not None)

        if field_count == 0:
            raise EmptyFieldValueError("all fields are empty")

        if field_count != 1:
            raise MultipleFieldValueError("only one field must be filled")