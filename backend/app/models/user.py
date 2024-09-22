from datetime import datetime, timezone
from uuid import uuid4

from passlib.context import CryptContext
from sqlalchemy import Column, Integer, String, DATETIME

from backend.app.utils.database import Base

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], default="pbkdf2_sha256")


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    unique_id = Column(String(length=36), nullable=False, unique=True, default=str(uuid4()), index=True)

    created_at = Column(
        DATETIME(timezone=True), nullable=False, default=datetime.now(timezone.utc)
    )
    updated_at = Column(
        DATETIME(timezone=True), nullable=False, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc)
    )

    def hash_password(self, password):
        return pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)
