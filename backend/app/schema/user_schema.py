from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserLoginRequestSchema(BaseModel):
    email: EmailStr
    password: str


class UserCreateRequestSchema(UserLoginRequestSchema):
    first_name: str
    last_name: str
    username: Optional[str] = None


class UserUpdateSchema(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None


class UserResponseSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: Optional[str] = None
    email: EmailStr
    unique_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
