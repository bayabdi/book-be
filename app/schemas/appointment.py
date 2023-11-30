from datetime import datetime
from pydantic import BaseModel


class AppointmentBase(BaseModel):
    duration: int
    startTime: datetime
    reason: str
    status: int


class Appointment(AppointmentBase):
    id: int
