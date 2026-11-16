from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

tovar = {}

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_expired: bool = False

@app.post("/items/")
async def creator(it: Item) -> dict[str, int | Item]:
    num = len(tovar) + 1
    tovar[num] = it
    return {"id": num, "item": it}

@app.delete("/items/{item_id}")
async def deleter(item_id: int) -> dict[str, str]:
    if item_id in tovar:
        del tovar[item_id]
        return {"result": "ok"}
    raise HTTPException(status_code=404, detail="item_id is not exists")  