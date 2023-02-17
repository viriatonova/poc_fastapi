from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src.User import user_model


def get_user_by_email(db: Session, email: str):
    db_person = db.query(user_model.Person).filter(user_model.Person.email == email).first()
    return db_person
