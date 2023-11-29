from typing import Any, Dict, List, Optional, Union

from app.models.appointment import Appointment
from pydantic.types import UUID4
from sqlalchemy.orm import Session

def add(db: Session, email: str):
    print("OK")
