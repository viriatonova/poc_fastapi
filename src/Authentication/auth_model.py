from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        func)

from api.database import BASE


class Auth(BASE):
    __tablename__ = "auth"
    pass
