from typing import Any, List

from app.api import deps
from app import crud
from app.schemas import AppointmentBase
from app.core.security import password_hash, verify_password, create_jwt_token, get_current_user

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
    print(type(user.id))

    return crud.appointment.add(db, model, user.id)


@router.get("/list")
def list_by_email(
        email: str = Depends(get_current_user),
        db: Session = Depends(deps.get_db)
) -> Any:

    return crud.appointment.list_by_email(db, email)
