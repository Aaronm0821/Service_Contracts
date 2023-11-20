from pydantic import BaseModel
from datetime import datetime

class ContractsBase(BaseModel):
    id: int
    service_contract: str
    start_date: datetime
    end_date: datetime
    last_PM: datetime
    next_PM: datetime
    machine_id: int

