from pydantic import BaseModel


class Page(BaseModel):
    items: list
    total: int
    page: int
    size: int