from typing import Any, Dict, List, Optional, Union

from app.models.appointment import Appointment
from app.models.user import User
from app.schemas.appointment import AppointmentBase, Appointment as AppointmentView
from sqlalchemy.orm import Session


def add(db: Session, model: AppointmentBase, user_id):
    print(model, user_id)
    db_model = Appointment(
        duration=model.duration,
        reason=model.reason,
        start_time=model.startTime,
        status=model.status,
        user_id=user_id
    )

    db.add(db_model)
    db.commit()


def list_by_email(db: Session, email: str):
    result = (
        db.query(
            Appointment.id,
            Appointment.start_time,
            Appointment.duration,
            Appointment.reason,
            Appointment.status
        )
        .join(User, Appointment.user_id == User.id)
        .filter(User.email == email)
        .all()
    )

    appointments = []

    for row in result:
        appointments.append(AppointmentView(
            id=row.id,
            startTime=row.start_time,
            duration=row.duration,
            reason=row.reason,
            status=row.status,
        ))

    return appointments