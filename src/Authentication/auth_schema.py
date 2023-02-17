from pydantic import BaseModel


class AuthBase(BaseModel):
    access_token: str
    token_type: str

        