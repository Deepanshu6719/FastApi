from fastapi import FastAPI
from pydantic import BaseModel, Field

app=FastAPI()

class CategoryRequest(BaseModel):
    name:str

class CategoryResponse(BaseModel):
    id:int
    name:str

class ProductRequest(BaseModel):
    name:str
    price:float
    in_stock:bool
    tags:list[str]=Field(default_factory=list)
    category:CategoryRequest

class ProductResponse(BaseModel):
    id:int
    name:str
    price:float
    tags:list[str]
    category:CategoryResponse


@app.post("/products",response_model=ProductResponse)
def create_product(product:ProductRequest):
    return{
        "id":1,
        "name":product.name,
        "price":product.price,
        "in_stock":product.in_stock,
        "tags":product.tags,
        "category":{
            "id":10,
            "name":product.category.name
        }
    }

@app.get("/products",response_model=list[ProductResponse])
def get_products():
    return[
        {
            "id": 1,
            "name": "Laptop",
            "price": 50000,
            "in_stock": True,
            "tags": ["electronics", "computer"],
            "category": {
                "id": 10,
                "name": "Electronics"
            }
        },
        {
            "id": 2,
            "name": "Mouse",
            "price": 500,
            "in_stock": True,
            "tags": ["accessories"],
            "category": {
                "id": 11,
                "name": "Computer Accessories"
            }
        }
    ]