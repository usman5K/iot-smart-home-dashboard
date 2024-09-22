from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.crud.user_crud import update_user
from backend.app.models import User
from backend.app.schema.user_schema import UserResponseSchema, UserUpdateSchema
from backend.app.utils.auth import get_authenticated_user
from backend.app.utils.database import get_db

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/me", status_code=200, response_model=UserResponseSchema)
async def get_me(
        user: User = Depends(get_authenticated_user)
):
    return user


@router.put("/me", status_code=200, response_model=UserResponseSchema)
async def update_me(
        payload: UserUpdateSchema,
        user: User = Depends(get_authenticated_user),
        db: Session = Depends(get_db),
):
    user = update_user(db, user.id, payload)
    return user


@router.delete("/me", status_code=204)
async def delete_me(
        user: User = Depends(get_authenticated_user),
        db: Session = Depends(get_db)
):
    db.delete(user)
    db.commit()
    return None
