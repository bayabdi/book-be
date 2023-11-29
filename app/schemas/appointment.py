from datetime import datetime
from pydantic import BaseModel


class AppointmentBase(BaseModel):
    Duration: int
    StartTime: datetime
    Reason: str
    Status: int
