from fastapi import FastAPI, Cookie, Response

app = FastAPI()

@app.get("/visit")
async def schet(resp: Response, info: str = Cookie(None)) -> dict:
    if info:
        count = int(info) + 1
    else:
        count = 0
    resp.set_cookie("visit", str(count), max_age=3600, httponly=True)
    return {"visits": count}