from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        func)

from api.database import BASE


class User(BASE):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    active = Column(Boolean, default=True)
    checked = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    excluded_at = Column(DateTime(timezone=True), nullable=True)
