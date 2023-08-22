from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from api.database import get_db
from api.exceptions import credentials_exception, inative_user
from api.settings import ALGORITHM, SECRET_KEY
from src.User.user_model import User
from src.User.user_schema import UserIn

pwd_context = CryptContext(schemes=['bcrypt'])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

# Authentication

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

def authenticate_user(db: Session, username: str, password: str):
    db_user = get_user_by_username(db, username)
    if not db_user:
        return False
    if not verify_password(password, db_user.password):
        return False
    #TODO feature: check e-mail msg:descomentar quando implementar a feature
    # if db_user.checked != True:
    #     return False
    return db_user

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("user")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    db_user = get_user_by_username(db, token_data.username)
    if db_user is None:
        raise credentials_exception
    return db_user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.active:
        raise inative_user
    return current_user

def get_all_user(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    return db_user

def get_user_by_email(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
    return db_user

def get_user_by_username(db: Session, username: str):
    db_user = db.query(User).filter(User.username == username).first()
    return db_user

def create_db_user(db: Session, user: UserIn):
    try:
        user.password = create_hash(user.password)
        db_user = User(
            username = user.username,
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
            password = user.password 
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except (IntegrityError) as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'A database error occurred: {error.orig}')
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(error))

def update_db_user(db: Session, user: UserIn, id: int):
    db.query(User).filter(User.id == id).update(user)
    db.commit()
    return None

def delete_db_user(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    db_user.active = False
    db.commit()
    db.refresh(db_user)
    return db_user

