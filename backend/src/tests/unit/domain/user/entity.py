from datetime import datetime
import uuid

from dataclasses import dataclass, field

from backend.domain.shared.value_objects.email.value_objects import Email
from tests.unit.domain.shared.value_objects.username.value_objects import Username


@dataclass
class User:
    id: uuid.UUID
    first_name: str # Name
    last_name: str # Name
    username: Username # Username
    email: Email # Email
    password_hash: str
    last_interaction: datetime
    is_active: bool = field(default=True)
    created_at: datetime = field(default=datetime.now)
    updated_at: datetime = field(default=datetime.now)

