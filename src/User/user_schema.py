from datetime import datetime

from pydantic import BaseModel


class UserIn(BaseModel):
   id: int | None = None 
   first_name: str
   last_name: str
   email: str
   password: str
   active: bool | None = None
   created_at: datetime | None = None
   excluded_at: datetime | None = None

class UserOut(BaseModel):
   email: str
   created_at: datetime | None = None
        