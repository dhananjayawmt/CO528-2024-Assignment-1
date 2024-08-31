from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import json
import os

app = FastAPI()

# Define a Pydantic model for the item
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

# Path to the JSON file
JSON_FILE_PATH = "items.json"

# Load data from JSON file
def load_items() -> List[Item]:
    if not os.path.exists(JSON_FILE_PATH):
        return []
    with open(JSON_FILE_PATH, "r") as file:
        items = json.load(file)
        return [Item(**item) for item in items]

# Save data to JSON file
def save_items(items: List[Item]) -> None:
    with open(JSON_FILE_PATH, "w") as file:
        json.dump([item.dict() for item in items], file, indent=4)

# In-memory database initialized from JSON
items_db: List[Item] = load_items()

# CRUD Operations

# Create an item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    # Check if the item ID already exists
    for existing_item in items_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    items_db.append(item)
    save_items(items_db)
    return item

# Read all items
@app.get("/items/", response_model=List[Item])
def read_items():
    return items_db

# Read a single item by ID
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Update an item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            save_items(items_db)
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            save_items(items_db)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
