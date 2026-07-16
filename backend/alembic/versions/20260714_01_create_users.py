"""create users table

Revision ID: 20260714_01
Revises:
Create Date: 2026-07-14
"""

import sqlalchemy as sa
from alembic import op


revision = "20260714_01"
down_revision = None
branch_labels = None
depends_on = None


user_role = sa.Enum(
    "SUPER_ADMIN",
    "ADMIN",
    "SECRETARIA",
    "FINANCEIRO",
    "SENSEI",
    "INSTRUTOR",
    "ALUNO",
    "RESPONSAVEL",
    name="user_role",
    create_type=False,
)


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("full_name", sa.String(length=255), nullable=False),
        sa.Column("hashed_password", sa.String(length=255), nullable=False),
        sa.Column("role", user_role, nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("last_login", sa.DateTime(timezone=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")
    
