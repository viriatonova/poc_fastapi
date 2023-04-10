from datetime import datetime

from pydantic import BaseModel


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
        orm_mode = True

class UserRead(UserBase):
    class Config:
        fields = {}

class UserCreate(UserBase):
    class Config:
        fields = {
            'id': {'exclude': True}, 'active': {'exclude': True},
            'created_at': {'exclude': True}, 'excluded_at': {'exclude': True}
        }
        
class UserUpdate(UserBase):
     class Config:
        fields = {
            'id': {'exclude': True}, 'active': {'exclude': True},
            'created_at': {'exclude': True}, 'excluded_at': {'exclude': True}
        }
        