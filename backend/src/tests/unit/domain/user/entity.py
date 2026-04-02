from ast import Name
from datetime import datetime
import uuid

from dataclasses import dataclass, field

from backend.domain.shared.value_objects.email.value_objects import Email
from tests.unit.domain.shared.value_objects.username.value_objects import Username


@dataclass
class User:
    id: uuid.UUID
    first_name: Name # Name
    last_name: Name # Name
    username: Username # Username
    email: Email # Email
    password_hash: str
    last_interaction: datetime | None = None
    is_active: bool = field(default=True)
    created_at: datetime = field(default=datetime.now)
    updated_at: datetime = field(default=datetime.now)


    @property
    def full_name(self):
        """
        Свойства которое возврщает полное имя поль.
        :return:
        """
        return f"{self.first_name} {self.last_name}"

    def touch(self):
        """
        Будет фиксировать время изменения
        :return:
        """
        self.updated_at = datetime.now()

    def interacts(self):
        """
        Будет фиксировать время последной активности
        :return:
        """
        self.last_interaction = datetime.now()


    def ensure_active(self):
        """
        Будет проверять что поль. активен
        :return:
        """
        if not self.is_active:
            raise


    @classmethod
    def create(
            cls,
            id: uuid.UUID,
            first_name: str,
            last_name: str,
            username: str,
            email: str,
            password_hash: str,
    ):
        """
        Создаёт объект поль.
        :param id: Уникальный Идентификатор
        :param first_name: Имя поль.
        :param last_name: фамилия поль.
        :param username: Юзурнейм
        :param email: Электронная почта
        :param password_hash: Захершированный пароль
        :return:  Объект поль.
        """
        return cls(
            id=id,
            first_name=Name(first_name),
            last_name=Name(last_name),
            username=username,
            email=email,
            password_hash=password_hash,
        )

    def __hash__(self):
        return hash(self.id)


