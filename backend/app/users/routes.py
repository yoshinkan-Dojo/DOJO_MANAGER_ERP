import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.auth.dependencies import AdminUser, CurrentUser
from app.database.session import get_db
from app.users.models import UserRole
from app.users.repositories import UserRepository
from app.users.schemas import UserCreate, UserRead, UserUpdate
from app.users.services import UserAlreadyExistsError, UserService


router = APIRouter(prefix="/users", tags=["Users"])
DbSession = Annotated[Session, Depends(get_db)]


def get_service(db: DbSession) -> UserService:
    return UserService(UserRepository(db))


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED, summary="Create a user")
def create_user(payload: UserCreate, _: AdminUser, db: DbSession) -> UserRead:
    try:
        return UserRead.model_validate(get_service(db).create_user(payload))
    except UserAlreadyExistsError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered") from None


@router.get("", response_model=list[UserRead], summary="List users")
def list_users(
    _: AdminUser,
    db: DbSession,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
) -> list[UserRead]:
    return [UserRead.model_validate(user) for user in get_service(db).list_users(offset, limit)]


@router.get("/{user_id}", response_model=UserRead, summary="Get a user")
def get_user(user_id: uuid.UUID, current_user: CurrentUser, db: DbSession) -> UserRead:
    is_admin = current_user.is_superuser or current_user.role in {
        UserRole.SUPER_ADMIN,
        UserRole.ADMIN,
    }
    if current_user.id != user_id and not is_admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
    user = get_service(db).get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return UserRead.model_validate(user)


@router.patch("/{user_id}", response_model=UserRead, summary="Partially update a user")
def update_user(user_id: uuid.UUID, payload: UserUpdate, _: AdminUser, db: DbSession) -> UserRead:
    service = get_service(db)
    user = service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    try:
        return UserRead.model_validate(service.update_user(user, payload))
    except UserAlreadyExistsError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered") from None


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a user")
def delete_user(user_id: uuid.UUID, _: AdminUser, db: DbSession) -> None:
    service = get_service(db)
    user = service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    service.delete_user(user)
    return None
