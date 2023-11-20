from typing import Optional

from pydantic import BaseModel


class Reps(BaseModel):
    id: int
    rep_first_name: str
    rep_last_name: str
    rep_email: str


class RepsCreate(BaseModel):
    rep_first_name: str
    rep_last_name: str
    rep_email: str
