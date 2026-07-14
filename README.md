# DOJO_MANAGER ERP

> Enterprise Resource Planning for Martial Arts Organizations

## Visão

O **DOJO_MANAGER ERP** é uma plataforma corporativa especializada na
gestão de escolas e organizações de artes marciais, iniciando pelo
**Yoshinkan Dojo**.

## Objetivos

-   Gestão Acadêmica
-   Gestão Financeira
-   Document Center
-   CRM
-   Estoque e Patrimônio
-   Dashboard Executivo
-   Multi-tenant
-   APIs para integrações

## Arquitetura e stack oficial

-   Clean Architecture, Domain-Driven Design (DDD) e SOLID como diretrizes
-   Python 3.13+
-   FastAPI e Uvicorn para a API
-   PostgreSQL como banco de dados relacional
-   SQLAlchemy como ORM e Alembic para migracoes
-   Pydantic Settings para configuracao por ambiente
-   `uv`, `pyproject.toml` e `uv.lock` como fonte de verdade das dependencias

## Estrutura do Projeto

```text
backend/
  app/
    api/
    core/
    database/
  alembic/
docker-compose.yml
```

## Execucao local

1. Copie `backend/.env.example` para `backend/.env` e substitua as credenciais de exemplo.
2. Na raiz do projeto, suba o PostgreSQL com `docker compose --env-file backend/.env up -d`.
3. No diretorio `backend`, sincronize o ambiente com `uv sync` e inicie a API com
   `uv run uvicorn app.main:app --reload`.

## Roadmap

-   v0.9.0-alpha -- Foundation Repository
-   v0.9.x -- Banco de Dados
-   v1.0.0 -- MVP
-   v2.0.0 -- Release Comercial

## Licença

Inicialmente distribuído sob a licença MIT.

------------------------------------------------------------------------

**Autor do Projeto:** Fabiano Caires\
**Projeto:** DOJO_MANAGER ERP
