from app import crud, schemas
from app.constants.role import Role
from app.core.config import settings
from sqlalchemy.orm import Session


def init_db(db: Session) -> None:

    print("IN THIS PLACE ---> ")