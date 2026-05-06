from pydantic import BaseModel


class RenameCustomFieldCommand(BaseModel):
    name: str