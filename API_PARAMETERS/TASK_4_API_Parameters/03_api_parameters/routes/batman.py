# from fastapi import APIRouter, Path, Query, Body
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float

# router = APIRouter()

# @router.get("/items/{item_id}")
# async def get_item(
#     item_id: int = Path(..., title="Item ID", ge=1),
# ):
#     return {"message": f"Path parameter received", "item_id": item_id}


# @router.get("/items/")
# async def list_items(
#     q: str | None = Query(None, min_length=3, max_length=50, title="Search query"),
#     skip: int = Query(0, ge=0),
#     limit: int = Query(10, le=100)
# ):
#     return {"message": "Query parameters received", "q": q, "skip": skip, "limit": limit}


# @router.put("/items/validated/{item_id}")
# async def update_item(
#     item_id: int = Path(..., ge=1),
#     q: str | None = Query(None, min_length=3),
#     item: Item | None = Body(None)
# ):
#     result = {"message": "Path, Query & Body used", "item_id": item_id}
#     if q:
#         result["q"] = q
#     if item:
#         result["item"] = item.model_dump()
#     return result

 
from fastapi import APIRouter, Path, Query, Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float

router = APIRouter()

@router.get("/batman/{item_id}")
async def get_batman_item(
    item_id: int = Path(..., title="Item ID", ge=1),
):
    return {"message": f"Path parameter received", "item_id": item_id}

@router.get("/batman/")
async def list_batman_items(
    q: str | None = Query(None, min_length=3, max_length=50, title="Search query"),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100)
):
    return {"message": "Query parameters received", "q": q, "skip": skip, "limit": limit}

@router.put("/batman/validated/{item_id}")
async def update_batman_item(
    item_id: int = Path(..., ge=1),
    q: str | None = Query(None, min_length=3),
    item: Item | None = Body(None)
):
    result = {"message": "Path, Query & Body used", "item_id": item_id}
    if q:
        result["q"] = q
    if item:
        result["item"] = item.model_dump()
    return result
