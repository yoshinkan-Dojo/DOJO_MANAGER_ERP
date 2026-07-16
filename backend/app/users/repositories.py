import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.shared.repositories import BaseRepository
from app.users.models import User


class UserRepository(BaseRepository[User]):
    def __init__(self, db: Session):
        super().__init__(db)

    def get_by_id(self, user_id: uuid.UUID) -> User | None:
        return self.db.get(User, user_id)

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email.lower())
        return self.db.scalar(statement)

    def list(self, offset: int = 0, limit: int = 100) -> list[User]:
        statement = (
            select(User)
            .order_by(User.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        return list(self.db.scalars(statement))

    def save(self, user: User) -> User:
        return self.add(user)

    def delete(self, user: User) -> None:
        super().delete(user)