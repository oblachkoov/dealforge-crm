from uuid import UUID

from backend.src.backend.application.user.repository import UserRepository
from backend.src.backend.domain.user.entity import User


class FakeUserRepository(UserRepository):
    def __init__(self, user: User = None):
        self._user = user

    async def get_by_username(self, username:str) -> User:
        return self._user

    async def get_by_id(self, user_id: UUID) -> User:
        return self._user