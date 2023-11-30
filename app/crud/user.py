from typing import Any, Dict, List, Optional, Union

from app.models.user import User
from app.schemas.user import UserCreate, User as UserView
from pydantic.types import UUID4
from sqlalchemy.orm import Session


def get_by_email(db: Session, email: str) -> Optional[UserView]:
    db_user = db.query(User).filter(User.email == email).first()

    if db_user is not None:
        return UserView(
            id=str(db_user.id),
            is_manager=db_user.is_manager,
            email=db_user.email,
            full_name=db_user.full_name,
            phone_number=db_user.phone_number
        )

    return None


def get_by_email_with_password(db: Session, email: str) -> Optional[User]:
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
