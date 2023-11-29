from typing import Any, Dict, List, Optional, Union

from app.models.appointment import Appointment
from sqlalchemy.orm import Session


def add(db: Session, model: Appointment, email: str):
    print(model, email)
