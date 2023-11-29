from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr


# Shared properties
class AppointmentBase(BaseModel):
    email: EmailStr = None
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
