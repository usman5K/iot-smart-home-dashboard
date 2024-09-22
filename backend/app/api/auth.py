from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.crud.user_crud import get_user_by_email, create_user
from backend.app.models import User
from backend.app.schema.auth_schema import AuthLoginRequestSchema, AuthResponseSchema, AuthRegisterRequestSchema
from backend.app.schema.user_schema import UserResponseSchema
from backend.app.utils.auth import create_login_token
from backend.app.utils.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/login", status_code=200, response_model=AuthResponseSchema)
async def login(
        payload: AuthLoginRequestSchema,
        db: Session = Depends(get_db)
):
    db_user: User = get_user_by_email(db, payload.email)

    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    if not db_user.verify_password(payload.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    token = create_login_token({"unique_id": db_user.unique_id})

    return AuthResponseSchema(
        access_token=token,
        user=UserResponseSchema.model_validate(db_user)
    )


@router.post("/register", status_code=201, response_model=AuthResponseSchema)
async def register(
        payload: AuthRegisterRequestSchema,
        db: Session = Depends(get_db)
):
    db_user = get_user_by_email(db, payload.email)

    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already exists")

    user = create_user(db, payload)

    token = create_login_token({"unique_id": user.unique_id})

    return AuthResponseSchema(
        access_token=token,
        user=UserResponseSchema.model_validate(user)
    )
