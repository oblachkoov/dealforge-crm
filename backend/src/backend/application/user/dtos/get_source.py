from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class GetSourceCommand(BaseModel):
    source_id: UUID

class GetSourceResponse(BaseModel):
    source_id: UUID


class GetSourceResult(BaseModel):
    id: UUID
    name: str
    type: SourceType
    config: GetSourceConfigDTO
    is_active: bool
    is_deleted: bool
    created_at: datetime
    updated_at: datetime
