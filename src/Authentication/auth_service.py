from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext

from api.settings import ALGORITHM, SECRET_KEY
from src.User.user_service import get_user_by_email

pwd_context = CryptContext(schemes=['bcrypt'])


def verify_password(input_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(input_password, hashed_password)

def create_hash(input_password: str) -> str:
    return pwd_context.hash(input_password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def authenticate_user(fake_db, username: str, password: str):
    user = get_user_by_email(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user