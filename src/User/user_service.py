from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.User.user_model import User
from src.User.user_schema import UserCreate
from datetime import datetime, timedelta

from jose import JWTError, jwt
from passlib.context import CryptContext

from api.settings import ALGORITHM, SECRET_KEY

pwd_context = CryptContext(schemes=['bcrypt'])


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

def authenticate_user(db: Session, email: str, password: str):
    db_user = get_user_by_email(db, email)
    if not db_user:
        return False
    if not verify_password(password, db_user.password):
        return False
    return db_user

def get_all_user(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    return db_user

def get_user_by_email(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
    return db_user

def create_db_user(db: Session, user: UserCreate):
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

def update_db_user(db: Session, user: UserCreate, id: int):
    db.query(User).filter(User.id == id).update(user)
    db.commit()
    return None

def delete_db_user(db: Session, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    db_user.active = False
    db.commit()
    db.refresh(db_user)
    return db_user

