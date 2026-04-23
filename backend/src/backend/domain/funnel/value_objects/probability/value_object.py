from dataclasses import dataclass

from backend.src.backend.domain.funnel.value_objects.probability.errors import UnsupportedProbabilityTypeError, \
    OutOfRangeProbabilityError


@dataclass(frozen=True)
class Probability:
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise UnsupportedProbabilityTypeError()

        if not self.__validate():
            raise OutOfRangeProbabilityError()

    def __validate(self) -> bool:
        return 0 <= self.value <= 100