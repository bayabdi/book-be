from datetime import datetime
from pydantic import BaseModel


class AppointmentBase(BaseModel):
    duration: int
    startTime: datetime
    reason: str
    status: int


class Appointment(AppointmentBase):
    id: int


class AppointmentFull(Appointment):
    user_id: str
    fullName: str
    email: str
    phoneNumber: str


class ChangeStatus(BaseModel):
    id: int
    status: int


class Interval(BaseModel):
    startTime: datetime
    duration: int
