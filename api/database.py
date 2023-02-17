from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.settings import DB_DATABASE, DB_HOST, DB_PASSWORD, DB_SERVER, DB_USER

# Database MySQL
DB = f"{DB_SERVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
ENGINE = create_engine(DB)
SESSION = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
BASE = declarative_base()


def get_db():
    db = SESSION()
    try:
        yield db
    finally:
        db.close()

