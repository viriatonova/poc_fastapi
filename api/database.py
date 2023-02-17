from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Database MySQL
DB_CTI = f"{DB_SERVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST_CTI}/{DB_DATABASE_CTI}"
ENGINE_CTI = create_engine(DB_CTI)
SESSION_CTI = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE_CTI)
BASE = declarative_base()


def get_db():
    db = SESSION_CTI()
    try:
        yield db
    finally:
        db.close()

