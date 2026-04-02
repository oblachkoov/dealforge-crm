from typing import Protocol

from backend.src.backend.application.repositories.user_repo import UserRepository


class UnitOfWork(Protocol):
    users: UserRepository

    async def commit(self) -> None:
        pass

    async def rollback(self) -> None:
        pass

    async def __aenter__(self):
        pass

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass