from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from pydantic import BaseModel, HttpUrl
import random
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

codes = {}
chars = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

@app.post("/shorten/{url:path}")
async def shorter(url: HttpUrl) -> dict[str, str]:
    code = ""
    for i in range(6):
        code += f"{random.choice(chars)}"
    codes[code] = url
    asyncio.create_task(deleter(code))
    return {"og_url": url, "short_url": code}

@app.get("/{code}")
async def get_url(code: str):
    if code in codes:
        return RedirectResponse(codes[code])
    raise HTTPException(status_code=404, detail="code is invalid")

async def deleter(cod):
    await asyncio.sleep(300)
    del codes[cod]