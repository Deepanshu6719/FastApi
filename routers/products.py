from fastapi import APIRouter,HTTPException
from models.schema import ProductRequest
router=APIRouter()

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 1000},
    {"id": 3, "name": "Keyboard", "price": 2000},
]


@router.get("/products/{product_id}")
def get_product_by_id(product_id:int):
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(
        status_code=404,
        detail="product not found"
    )

@router.post("/products",status_code=201)
def create_product(product:ProductRequest):
    return product
