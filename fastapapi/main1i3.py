from fastapi import FastAPI, Query
from typing import Annotated

import time, random

app = FastAPI()
info = {}

@app.get("/weather")
async def ww(q: Annotated[str, Query(min_length=1)]) -> dict:
    date = time.time()
    if q in info and date - info[q]["saved_at"] < 5:
        return {q: info[q], "cached": True}

    temp = random.randint(-20, 40)
    info[q] = {"temperature": temp, "saved_at": date}
    return {q: info[q], "cached": False}