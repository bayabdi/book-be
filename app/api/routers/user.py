from typing import Any, List

from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/test", response_model=str)
def test(
        db: Session = Depends(deps.get_db),
) -> Any:
    return "OK"
