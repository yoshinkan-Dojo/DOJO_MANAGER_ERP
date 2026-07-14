"""
DOJO_MANAGER ERP
Backend Foundation v0.9.1

Primeira aplicação FastAPI do projeto.
"""

from fastapi import FastAPI

app = FastAPI(
    title="DOJO_MANAGER ERP",
    version="0.9.1",
    description="ERP especializado para gestão de escolas de artes marciais."
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "project": "DOJO_MANAGER ERP",
        "version": "0.9.1"
    }
