from pydantic import BaseModel, EmailStr

from backend.app.schema.user_schema import UserResponseSchema


class AuthRegisterRequestSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class AuthLoginRequestSchema(BaseModel):
    email: EmailStr
    password: str


class AuthResponseSchema(BaseModel):
    access_token: str
    user: UserResponseSchema

    class Config:
        from_attributes = True
