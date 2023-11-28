from typing import Any, Dict, List, Optional, Union

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from pydantic.types import UUID4
from sqlalchemy.orm import Session


def get_by_email(db: Session, email: str) -> Optional[User]:
    return db.query(User).filter(User.email == email).first()


def create(db: Session, model: UserCreate):
    db_model = User(
        full_name=model.full_name,
        email=model.email,
        phone_number=model.phone_number,
        hashed_password=model.password
    )

    db.add(db_model)
    db.commit()
