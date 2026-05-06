from uuid import UUID

from pydantic import BaseModel


class GetCustomFieldByIdCommand(BaseModel):
    id: UUID