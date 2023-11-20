from pydantic import BaseModel
from datetime import datetime


class MachinesBase(BaseModel):
    id: int
    machine_type: str
    serial_number: str
    install_date: datetime
    site_survery_OCC: str
    install_OCC: str
    customer_id: int