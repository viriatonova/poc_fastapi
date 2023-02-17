from pydantic import BaseModel


class AuthBase(BaseModel):
    pass

class AuthRead(AuthBase):
    pass

class AuthCreate(AuthBase):
    pass
        
class AuthUpdate(AuthBase):
    pass

        