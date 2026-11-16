from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Zadacha(BaseModel):
    a: float = 0
    b: float = 0
    action: str

@app.post("/calculate/")
async def calc(primer: Zadacha) -> dict[str, float]:
    if primer.action == "add":
        return {"result": primer.a+primer.b}
    elif primer.action == "subtract":
        return {"result": primer.a-primer.b}
    
    if primer.a == 0 or primer.b == 0:
        raise HTTPException(status_code=400, detail="Нельзя умножить/делить на 0")
    
    if primer.action == "multiply":
        return {"result": round(primer.a*primer.b, 2)}
    elif primer.action == "devide":
        return {"result": round(primer.a/primer.b, 2)}