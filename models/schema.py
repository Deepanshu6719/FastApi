from pydantic import BaseModel, Field
from datetime import date

class CategoryRequest(BaseModel):
    name: str


class CategoryResponse(BaseModel):
    id: int
    name: str


class ProductRequest(BaseModel):
    name: str
    price: float
    in_stock: bool
    tags: list[str] = Field(default_factory=list)
    category: CategoryRequest


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool
    tags: list[str]
    category: CategoryResponse

class TaskCreate(BaseModel):
    title:str
    description:str
    status:str
    due_date:date

class TaskUpdate(BaseModel):
    title:str | None = None
    description:str | None = None
    status:str | None = None
    due_date:date | None = None

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: str
    due_date: date

    class Config:
        from_attributes = True