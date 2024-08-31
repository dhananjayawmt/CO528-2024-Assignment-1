from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

JSON_FILE_PATH = "items.json"

def load_items() -> List[Item]:
    if not os.path.exists(JSON_FILE_PATH):
        return []
    with open(JSON_FILE_PATH, "r") as file:
        items = json.load(file)
        return [Item(**item) for item in items]

def save_items(items: List[Item]) -> None:
    with open(JSON_FILE_PATH, "w") as file:
        json.dump([item.dict() for item in items], file, indent=4)

items_db: List[Item] = load_items()

# CRUD Operations

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    for existing_item in items_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    items_db.append(item)
    save_items(items_db)
    return item

@app.get("/items/", response_model=List[Item])
def read_items():
    return items_db

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            save_items(items_db)
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            save_items(items_db)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
