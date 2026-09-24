from fastapi import APIRouter

router=APIRouter()

@router.get("/categories")
def get_category():
    return{
        "categories":[
            {"id": 1, "name": "Electronics"},
            {"id": 2, "name": "Books"}
        ]
    }