from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import CurrentUser
from app.auth.schemas import LoginRequest, RefreshRequest, TokenPair
from app.auth.services import build_token_pair, validate_refresh_token
from app.database.session import get_db
from app.users.repositories import UserRepository
from app.users.services import UserService


router = APIRouter(prefix="/auth", tags=["Authentication"])
DbSession = Annotated[Session, Depends(get_db)]


@router.post("/login", response_model=TokenPair, summary="Authenticate a user")
def login(payload: LoginRequest, db: DbSession) -> TokenPair:
    user = UserService(UserRepository(db)).authenticate(payload.email, payload.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return TokenPair(**build_token_pair(user))


@router.post("/refresh", response_model=TokenPair, summary="Refresh an access token")
def refresh(payload: RefreshRequest, db: DbSession) -> TokenPair:
    user = UserRepository(db).get_by_id(validate_refresh_token(payload.refresh_token))
    if user is None or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid refresh token")
    return TokenPair(**build_token_pair(user))


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT, summary="Log out the current user")
def logout(_: CurrentUser) -> None:
    """Stateless logout: clients must discard their access and refresh tokens."""
    return None


@router.get("/me", summary="Return the authenticated user")
def read_current_user(current_user: CurrentUser):
    return current_user
