from fastapi import Depends, HTTPException, status

from app.auth.dependencies import get_current_user
from app.users.models import User, UserRole


def require_super_admin(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role != UserRole.SUPER_ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied",
        )
    return current_user


def require_admin(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role not in (
        UserRole.SUPER_ADMIN,
        UserRole.ADMIN,
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied",
        )
    return current_user


def require_secretaria(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role not in (
        UserRole.SUPER_ADMIN,
        UserRole.ADMIN,
        UserRole.SECRETARIA,
    ):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Permission denied",
        )
    return current_user