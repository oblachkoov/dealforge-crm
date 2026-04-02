from typing import Protocol
from uuid import UUID

from backend.src.tests.unit.domain.user.entity import User


class UserRepository(Protocol):
    """
    Interface for user repository
    """
    async def get_by_username(self, username: str) -> User:
        pass

    async def get_by_email(self, email: str) -> User:
        pass


    async def get_by_id(self, id: UUID) -> User:
        pass


    async def create(self, user: User) -> User:
        pass


    async def update(self, user: User) -> None:
        pass

    async def delete(self, user: User) -> None:
        pass