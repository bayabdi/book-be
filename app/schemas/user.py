from datetime import datetime
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: EmailStr = None
    full_name: Optional[str] = None
    phone_number: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class LoginModel(BaseModel):
    email: str
    password: str


# Model for JWT token
class TokenData:
    sub: str = None
    username: str = None
    is_manager: bool = False
