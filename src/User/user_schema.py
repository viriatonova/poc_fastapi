from datetime import datetime

from pydantic import BaseModel
from typing import Union



class UserBase(BaseModel):
   id: int | None = None
   username: str
   first_name: str
   last_name: str
   email: str
   password: str
   active: bool | None = None
   created_at: datetime | None = None
   excluded_at: datetime | None = None

   class Config:
        pass

class UserRead(UserBase):
    class Config:
        orm_mode = True
        fields = {}

class UserCreate(UserBase):
    class Config:
        orm_mode = True
        fields = {
            'id': {'exclude': True}, 'active': {'exclude': True},
            'created_at': {'exclude': True}, 'excluded_at': {'exclude': True}
        }
        
class UserUpdate(UserBase):
     class Config:
        orm_mode = True
        fields = {
            'id': {'exclude': True}, 'active': {'exclude': True},
            'created_at': {'exclude': True}, 'excluded_at': {'exclude': True}
        }

# Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None


        