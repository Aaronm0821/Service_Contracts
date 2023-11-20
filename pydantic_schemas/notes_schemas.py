from pydantic import BaseModel


class NotesBase(BaseModel):
    id: int
    note: str
    machine_id: int
