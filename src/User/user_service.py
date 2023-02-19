from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from src.User.user_model import User
from src.User.user_schema import UserCreate

from src.User import user_model


def get_all_user(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, id: int):
    db_person = db.query(user_model.Person).filter(user_model.Person.id == id).first()
    return db_person

def get_user_by_email(db: Session, email: str):
    db_person = db.query(user_model.Person).filter(user_model.Person.email == email).first()
    return db_person

def create_db_user(db: Session, user: UserCreate):
    try:
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
