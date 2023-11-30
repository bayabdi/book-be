from app.core.config import settings

from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from passlib.context import CryptContext


# OAuth2PasswordBearer for token handling
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password hashing
password_hash = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Function to create JWT token
def create_jwt_token(data: dict) -> str:
    to_encode = data.copy()
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


# Function to verify password
def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)


# Function to get current user
def get_current_user(
        token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=401, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username


# Function to get current manager
def get_current_manager(
        token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=401, detail="Could not validate credentials for manager", headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        is_manager: bool = payload.get("is_manager")

        if username is None or (not is_manager):
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username
