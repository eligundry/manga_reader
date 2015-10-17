from datetime import datetime

from sqlalchemy import create_engine, func, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import SQLITE_DB_LOCATION

def setup_database(db_location=SQLITE_DB_LOCATION):
    engine = create_engine(SQLITE_DB_LOCATION)
    session_factory = sessionmaker(bind=engine)
    db = session_factory()

    return engine, db

engine, db = setup_database()

# Base model for all models
Base = declarative_base()

class IDMixin(object):
    """
    Adds an integer primary key to a table
    """
    id = Column(Integer, primary_key=True)

class CreatedModifiedMixin(object):
    """
    Adds auto updating and creating of creation and modified timestamps
    """
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    modified = Column(DateTime, default=datetime.utcnow,
                      onupdate=func.current_timestamp(), nullable=False)

from application.models.manga_series import MangaSeries

__all__ = [
    'IDMixin',
    'CreatedModifiedMixin',
    'MangaSeries',
]
