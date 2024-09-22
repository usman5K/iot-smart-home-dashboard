from datetime import datetime, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from backend.app.crud.user_crud import get_user_by_unique_id
from backend.app.utils.database import get_db
from backend.app.utils.settings import logger

SECRET_KEY = "e8b3b0e7c7b5d4c6a8c3e8f7e4c7e8b3e7c3b5c7"
ALGORITHM = "HS256"

reusable_oauth2 = HTTPBearer()
TokenDep = Annotated[HTTPAuthorizationCredentials, Depends(reusable_oauth2)]


def get_authenticated_user(
        token: TokenDep,
        db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )

    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_unique_id: str = payload.get("unique_id")

        if user_unique_id is None:
            logger.error("JWT does not contain unique_id")
            raise credentials_exception

    except jwt.PyJWTError as err:
        logger.error(f"Decoding JWT failed: {err}")
        raise credentials_exception

    user = get_user_by_unique_id(db, unique_id=user_unique_id)

    if user is None:
        logger.error("Invalid token: User not found")
        raise credentials_exception

    return user


def create_login_token(data: dict) -> str:
    data["exp"] = datetime.now(timezone.utc).timestamp() + 3600
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
