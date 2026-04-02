from typing import Protocol


class Hasher(Protocol):
    """
    Interface for hasher
    """
    def hash(self, password: str) -> str:
        pass

    def verify(self, password: str, hashed_password: str) -> bool:
        pass
