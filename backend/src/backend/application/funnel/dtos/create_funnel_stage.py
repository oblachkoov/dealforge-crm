from uuid import UUID

from pydantic import BaseModel


class CreateFunnelStageCommand(BaseModel):
    name: str
    win_probability: int
    hex: str
    position: int | None = None

class CreateFunnelStageResult(BaseModel):
    stage_id: UUID