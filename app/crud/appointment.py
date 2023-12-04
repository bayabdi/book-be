from typing import Any, Dict, List, Optional, Union

from app.models.appointment import Appointment
from app.models.user import User
from datetime import datetime, timezone
from app.schemas.appointment import AppointmentBase,\
    Appointment as AppointmentView,\
    AppointmentFull, \
    ChangeStatus,\
    Interval
from sqlalchemy.orm import Session
from sqlalchemy import func


def add(db: Session, model: AppointmentBase, user_id):
    model.startTime = model.startTime.astimezone(timezone.utc)
    db_model = Appointment(
        duration=model.duration,
        reason=model.reason,
        start_time=model.startTime,
        status=model.status,
        user_id=user_id
    )

    db.add(db_model)
    db.commit()


def get_by_id(db: Session, appoint_id):
    return db.query(Appointment).filter(Appointment.id == appoint_id).first()


def list_by_email(db: Session, email: str, status: int):
    result = (
        db.query(
            Appointment.id,
            Appointment.start_time,
            Appointment.duration,
            Appointment.reason,
            Appointment.status
        )
        .join(User, Appointment.user_id == User.id)
        .filter(User.email == email, Appointment.status == status)
        .order_by(Appointment.start_time)
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


def list_by_status(db: Session, status: int):
    result = (
        db.query(
            Appointment.id,
            Appointment.start_time,
            Appointment.duration,
            Appointment.reason,
            Appointment.status,
            Appointment.user_id,
            User.full_name,
            User.email,
            User.full_name,
            User.phone_number
        )
        .join(User, Appointment.user_id == User.id)
        .filter(Appointment.status == status)
        .order_by(Appointment.start_time)
        .all()
    )

    appointments = []

    for row in result:
        appointments.append(AppointmentFull(
            id=row.id,
            startTime=row.start_time,
            duration=row.duration,
            reason=row.reason,
            status=row.status,
            user_id=str(row.user_id),
            fullName=row.full_name,
            email=row.email,
            phoneNumber=row.phone_number
        ))

    return appointments


def change_status(db: Session, model: ChangeStatus):
    db_model = db.query(Appointment).filter(Appointment.id == model.id).first()
    if db_model is not None:
        db_model.status = model.status
        db.commit()


def check_availability(db: Session, model: Interval):
    model.startTime = model.startTime.astimezone(timezone.utc)
    if datetime.now(timezone.utc) > model.startTime:
        return False

    begin_time = model.startTime.timestamp()
    end_time = begin_time + model.duration * 60

    query = (
        db.query(func.count(Appointment.id))
        .filter(
            func.greatest(func.extract('epoch', Appointment.start_time), begin_time) <= func.least(
                func.extract('epoch', Appointment.start_time) + Appointment.duration * 60, end_time),
            Appointment.status == 2  # approved status
        )
    )

    return query.scalar() < 1
