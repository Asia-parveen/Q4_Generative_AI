from fastapi import FastAPI, Path, Query, Header, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# 1. Path Parameter
# ------------------------------
@app.get("/path/{item_id}")
async def get_path(item_id: int = Path(..., title="Item ID", ge=1)):
    return {"message": f"Path parameter received here: {item_id}"}



# 2. Query Parameter
# ------------------------------
@app.get("/query/")
async def get_query(skip: int = Query(0), limit: int = Query(10)):
    return {"message": f"Query parameters received here: skip={skip}, limit={limit}"}



# 3. Request Body (JSON)
# ------------------------------
class Item(BaseModel):
    name: str
    price: float

@app.post("/body/")
async def create_item(item: Item):
    return {"message": f"Received item: {item.name} with price {item.price}"}



# 4. Header Parameter
# ------------------------------
@app.get("/header/")
async def read_header(user_agent: Optional[str] = Header(None)):
    return {"message": f"User-Agent received: {user_agent}"}



# 5. Combo: Path + Query
# ------------------------------
@app.get("/combo1/{item_id}")
async def combo1(
    item_id: int = Path(..., ge=1),
    limit: int = Query(10)
):
    return {"item_id": item_id, "limit": limit}



# 6. Combo: Query + Body
# ------------------------------
class Product(BaseModel):
    name: str
    price: float

@app.post("/combo2/")
async def combo2(
    discount: float = Query(0),
    product: Product = Body(...)
):
    return {
        "product": product.dict(),
        "discount": discount
    }



# 7. Combo: Path + Header
# ------------------------------
@app.get("/combo3/{id}")
async def combo3(
    id: int = Path(...),
    user_agent: Optional[str] = Header(None)
):
    return {"id": id, "user_agent": user_agent}

