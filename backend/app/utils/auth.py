from datetime import datetime, timezone
from typing import Annotated

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from backend.app.crud.user_crud import get_user_by_unique_id
from backend.app.utils.database import get_db
from backend.app.utils.settings import logger, base_settings

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
        payload = jwt.decode(token.credentials, base_settings.JWT_SECRET, algorithms=[ALGORITHM])
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
    return jwt.encode(data, base_settings.JWT_SECRET, algorithm=ALGORITHM)
