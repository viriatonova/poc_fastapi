from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from api.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from sqlalchemy.orm import Session
from src.User.user_model import User
from src.User.user_schema import UserCreate, UserRead, UserUpdate
from api.database import get_db
from src.User.user_service import *


router = APIRouter()

@router.get("/user/me/", response_model=UserRead)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@router.get("/user", status_code=status.HTTP_200_OK, response_model=list[UserRead])
def read_users(db: Session = Depends(get_db)):
    db_user = get_all_user(db)
    return db_user

@router.get("/user/{id}", status_code=status.HTTP_200_OK, response_model=UserRead)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, id=id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User dont't exist")
    else:
        return db_user

@router.post("/user", status_code=status.HTTP_201_CREATED, response_model=UserCreate)
def sing_up(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User alread exist")
    else:
        db_user = create_db_user(user=user, db=db)
        return db_user
    
@router.patch("/person/{id}", status_code=status.HTTP_206_PARTIAL_CONTENT, response_model=UserUpdate)
def update_person(id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, id=id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User dont't exist")
    else:
        user_data = user.dict(exclude_unset=True)
        update_db_user(user=user_data, db=db, id=id)
        return {"Successfully updated"}

@router.delete("/person/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=UserUpdate)
def delete_person(id: int, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, id=id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User alread exist")
    else:
        return delete_db_user(db=db, id=id)    

# Authentications Routes

@router.post("/token", response_model=Token)
async def get_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"user": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}