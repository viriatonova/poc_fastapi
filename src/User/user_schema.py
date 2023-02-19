from datetime import datetime

from pydantic import BaseModel, validator


class UserBase(BaseModel):
   id: int | None = None
   username: str
   first_name: str
   last_name: str
   email: str
   password: str
   active: bool
   created_at: datetime
   excluded_at: datetime

   class Config:
        pass

   @validator('created_at', 'excluded_at')
   def check_datetime(cls, field):
      if field <= datetime.now():
            raise ValueError('datetime_field must not be in the future')
      return field

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