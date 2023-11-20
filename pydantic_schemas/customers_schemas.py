from pydantic import BaseModel

class CustomerBase(BaseModel):
    id: int
    customer_name: str
    department: str
    location: str
    rep_id: int

