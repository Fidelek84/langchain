from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None
    description: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None
    description: Optional[str] = None


@app.get("/")
def home():
    return {"Data": "API Check!"}

@app.get("/abouut")
def about():
    return {"Data": "About Page"}

inventory = {
    1: {
        "name": "Gforce RTX 3080",
        "price": 999.90,
        "brand": "Nvidia"
    },
    2: {
        "name": "Ryzen 9 5900X",
        "price": 499.50,
        "brand": "AMD"
    },
    3: {
        "name": "Intel Core i9-12900K",
        "price": 589.00,
        "brand": "Intel"
    },
    4: {
        "name": "GeForce RTX 3070",
        "price": 599.99,
        "brand": "Nvidia"
    },
    5: {
        "name": "Radeon RX 6800 XT",
        "price": 649.00,
        "brand": "AMD"
    },
    6: {
        "name": "Kraken Z73 Liquid Cooler",
        "price": 279.99,
        "brand": "NZXT"
    },
    7: {
        "name": "G.Skill Trident Z RGB 16GB",
        "price": 89.99,
        "brand": "G.Skill"
    },
    8: {
        "name": "Samsung 970 EVO Plus 1TB SSD",
        "price": 99.99,
        "brand": "Samsung"
    },
    9: {
        "name": "ASUS ROG Strix B550-F Gaming",
        "price": 189.99,
        "brand": "ASUS"
    },
    10: {
        "name": "Corsair RM850x PSU",
        "price": 129.99,
        "brand": "Corsair"
    },
    11: {
        "name": "Logitech G Pro X Superlight Mouse",
        "price": 149.99,
        "brand": "Logitech"
    }
}
## GET
@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int, name: str):
    return inventory[item_id]

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]


@app.get("/get-by-name/{item_id}")
def get_item(*, name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not Found"}

## POST
@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    
    inventory[item_id] = item
    return inventory[item_id]

## PUT
@app.put("/create-item/{item_id}")
def create_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error": "Item ID does not exists."}
    
    if item.name != None:
        inventory[item_id].name = item.name
    
    if item.price != None:
        inventory[item_id].price = item.price  
    
    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

## DELETE
@app.delete("/create-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to delate", gt=0)):
    if item_id not in inventory:
        return {"Error": "Item ID does not exists."}
    
    del inventory[item_id]
    return {"Success": "Item deleted!"}