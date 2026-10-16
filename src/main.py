from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def healthApp() -> None:
    pass