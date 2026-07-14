import uuid

from fastapi import HTTPException, status
from jose import JWTError, jwt

from app.core.settings import get_settings
from app.shared.security import create_access_token, create_refresh_token
from app.users.models import User


def build_token_pair(user: User) -> dict[str, str]:
    return {
        "access_token": create_access_token(str(user.id), user.role.value),
        "refresh_token": create_refresh_token(str(user.id)),
        "token_type": "bearer",
    }


def validate_refresh_token(token: str) -> uuid.UUID:
    settings = get_settings()
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        if payload.get("type") != "refresh" or not (subject := payload.get("sub")):
            raise ValueError
        return uuid.UUID(subject)
    except (JWTError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from None
