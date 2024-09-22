from typing import Union

from sqlalchemy.orm import Session

from backend.app.models import User
from backend.app.schema.auth_schema import AuthRegisterRequestSchema
from backend.app.schema.user_schema import UserUpdateSchema


def get_user_by_email(db: Session, email: str) -> Union[User, None]:
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db: Session, user_id: int) -> Union[User, None]:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_unique_id(db: Session, unique_id: str) -> Union[User, None]:
    return db.query(User).filter(User.unique_id == unique_id).first()


def create_user(db: Session, user: AuthRegisterRequestSchema) -> User:
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email
    )
    db_user.password = db_user.hash_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user_id: int, user: UserUpdateSchema) -> User:
    db_user: User = get_user_by_id(db, user_id)

    if user.password:
        db_user.password = db_user.hash_password(user.password)

    for key, value in user.model_dump(exclude_none=True, exclude={"password"}).items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user_by_id(db, user_id)
    db.delete(db_user)
    db.commit()

    return db_user
