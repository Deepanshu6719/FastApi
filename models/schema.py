from pydantic import BaseModel, Field


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