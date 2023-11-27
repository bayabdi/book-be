import logging
from typing import Generator

from app import models, schemas
from app.constants.role import Role
from app.core import security
from app.core.config import settings
from app.db.session import SessionLocal
from fastapi import Depends, Request, HTTPException, Security, status
from pydantic import ValidationError
from sqlalchemy.orm import Session


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
