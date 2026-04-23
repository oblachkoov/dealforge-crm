from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from backend.src.backend.domain.shared.value_objects.email.value_object import Email
from backend.src.backend.domain.shared.value_objects.name.value_object import Name
from backend.src.backend.domain.user.entity import UserRole
from backend.src.backend.domain.user.value_objects.username.value_object import Username


class GetUserByIdCommand(BaseModel):
    user_id: UUID


class GetUserByIdResult(BaseModel):
    first_name: Name
    last_name: Name
    username: Username
    email: Email
    last_interaction: datetime | None
    is_active: bool
    role: UserRole

