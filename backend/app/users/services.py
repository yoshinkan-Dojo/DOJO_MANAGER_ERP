import uuid
from datetime import UTC, datetime

from app.shared.security import hash_password, verify_password
from app.users.models import User
from app.users.repositories import UserRepository
from app.users.schemas import UserCreate, UserUpdate


class UserAlreadyExistsError(Exception):
    """Raised when a requested email is already registered."""


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, payload: UserCreate) -> User:
        email = payload.email.lower()
        if self.repository.get_by_email(email):
            raise UserAlreadyExistsError("Email already registered")

        user = User(
            email=email,
            full_name=payload.full_name,
            hashed_password=hash_password(payload.password),
            role=payload.role,
            is_active=payload.is_active,
            is_superuser=payload.is_superuser,
        )
        return self.repository.save(user)

    def get_user(self, user_id: uuid.UUID) -> User | None:
        return self.repository.get_by_id(user_id)

    def list_users(self, offset: int = 0, limit: int = 100) -> list[User]:
        return self.repository.list(offset, limit)

    def update_user(self, user: User, payload: UserUpdate) -> User:
        changes = payload.model_dump(exclude_unset=True)
        if "email" in changes:
            email = changes["email"].lower()
            existing = self.repository.get_by_email(email)
            if existing and existing.id != user.id:
                raise UserAlreadyExistsError("Email already registered")
            user.email = email
            del changes["email"]
        if password := changes.pop("password", None):
            user.hashed_password = hash_password(password)
        for field, value in changes.items():
            setattr(user, field, value)
        return self.repository.save(user)

    def delete_user(self, user: User) -> None:
        self.repository.delete(user)

    def authenticate(self, email: str, password: str) -> User | None:
        user = self.repository.get_by_email(email.lower())
        if not user or not user.is_active or not verify_password(password, user.hashed_password):
            return None
        user.last_login = datetime.now(UTC)
        return self.repository.save(user)
