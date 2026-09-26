from fastapi import Depends,FastAPI
from routers.products import router as product_router
from routers.categories import router as category_router
from sqlalchemy.orm import Session
from database import get_db
from sqlalchemy import text
app=FastAPI()

# @app.get("/")
# def home():
#     return {"message":"Welcome"}
# print(app)

# # path parameter: resource identity identify a specific item , in url itself, no optional always mandatory or else will fail the url
# @app.get("/item/{item_id}")
# def get_item(item_id:int):
#     return {"item_id":item_id}

# #  query param: after ? in key:value pair , optional allowed, used for searchin , filtering like in ecomerce for product filtering
# @app.get("/search")
# def search(q:str):
#     return{"q":q}

# @app.get("/item_search/{item_id}")
# def search_item(item_id:int,q:str=""):
#     return {
#         "item_id":item_id,
#         "q":q
#     }


app.include_router(product_router)
app.include_router(category_router)

@app.get("/db-check")
def db_check(db:Session=Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    value = result.scalar()

    return {"database": value}