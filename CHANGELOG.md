# CHANGELOG

All notable changes to this project will be documented in this file.

The format follows **Keep a Changelog** and Semantic Versioning.

## [Unreleased]

### Changed

- Established FastAPI, PostgreSQL, SQLAlchemy, Alembic and `uv` as the official backend stack.
- Consolidated the FastAPI entry point at `backend/app/main.py`.
- Made SQL logging configurable by environment and disabled by default.
- Defined `pyproject.toml` and `uv.lock` as the dependency source of truth.

### Added

- Versioned Docker Compose and Alembic configuration for local database and migrations.
- Added Python/FastAPI `.gitignore` rules.

## \[0.9.0-alpha\] - 2026-07-10

### Added

-   Initial GitHub repository structure.
-   Initial README.
-   Project governance definition.
-   Clean Architecture and DDD guidelines.
-   Core modules definition.
-   Financial, Academic and Document Center planning.
-   Initial roadmap.
-   ADR process established.

### Planned

-   Master Document v0.9.0
-   Database model (MER)
-   PostgreSQL scripts
-   .NET solution structure
