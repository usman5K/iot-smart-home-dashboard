from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from backend.app.utils.settings import base_settings

SQLALCHEMY_DATABASE_URL =  base_settings.DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
