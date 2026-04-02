from typing import Protocol


class TokenService(Protocol):
    """
    Interface for TokenService
    """
    def encode(self, data: dict) -> str:
        pass

    def decode(self, token: str) -> dict:
        pass

    def get_token_type(self) -> str:
        pass