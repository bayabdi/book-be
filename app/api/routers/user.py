from typing import Any, List

from app.api import deps
from app import crud
from app.schemas import UserCreate, LoginModel, TokenData, User
from app.core.security import password_hash, verify_password, create_jwt_token, get_current_user

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/register", response_model=str)
def register(
        model: UserCreate,
        db: Session = Depends(deps.get_db),
) -> Any:
    if crud.user.get_by_email(db, model.email):
        raise HTTPException(status_code=400, detail="Username already registered")

    model.password = password_hash.hash(model.password)
    print(model.password)
    crud.user.create(db, model)

    print("OK")

    return "User registered successfully"


@router.post("/login", response_model=str)
def login(
        model: LoginModel,
        db: Session = Depends(deps.get_db),
) -> Any:
    user = crud.user.get_by_email_with_password(db, model.email)

    if (user is None) or (not verify_password(model.password, user.hashed_password)):
        raise HTTPException(status_code=401, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    token_data = {"sub": user.email, "username": user.email, "is_manager": user.is_manager}
    token = create_jwt_token(token_data)
    return token


@router.post("/test", response_model=User)
def test(
        email: str = Depends(get_current_user),
        db: Session = Depends(deps.get_db)

) -> Any:
    current_user = crud.user.get_by_email(db, email)
    print(current_user)
    return current_user
