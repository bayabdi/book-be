from typing import Any, List

from app.api import deps
from app import crud
from app.schemas import AppointmentBase, ChangeStatus, Interval
from app.core.security import get_current_user, get_current_manager
from app import services

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/appointment", tags=["appointment"])


@router.post("/add")
def add(
        model: AppointmentBase,
        email: str = Depends(get_current_user),
        db: Session = Depends(deps.get_db)
) -> Any:
    user = crud.user.get_by_email_with_password(db, email)

    if not crud.appointment.check_availability(db, Interval(
        startTime=model.startTime,
        duration=model.duration
    )):
        raise HTTPException(status_code=400, detail="Can't fit, choose other time")

    return crud.appointment.add(db, model, user.id)


@router.get("/list")
def list_by_email(
        status: int,
        email: str = Depends(get_current_user),
        db: Session = Depends(deps.get_db)
) -> Any:

    return crud.appointment.list_by_email(db, email, status)


@router.get("/list_by_status")
def list_by_status(
        status: int = 1,
        email: str = Depends(get_current_manager),
        db: Session = Depends(deps.get_db)
) -> Any:
    return crud.appointment.list_by_status(db, status)


@router.post("/change_status")
def change_status(
        model: ChangeStatus,
        email: str = Depends(get_current_manager),
        db: Session = Depends(deps.get_db)
) -> Any:

    appointment = crud.appointment.get_by_id(db, model.id)

    if appointment is None:
        raise HTTPException(status_code=404, detail="Not found")

    if model.status == 2:
        if not crud.appointment.check_availability(db, Interval(
            startTime=appointment.start_time,
            duration=appointment.duration
        )):
            raise HTTPException(status_code=400, detail="Can't fit, choose other time")
        else:
            services.google_calendar.add(appointment)

    return crud.appointment.change_status(db, model)


@router.post("/check_availability")
def check_availability(
    model: Interval,
    db: Session = Depends(deps.get_db)
) -> Any:
    return crud.appointment.check_availability(db, model)
