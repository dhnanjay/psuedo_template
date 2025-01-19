from fastapi import FastAPI

app = FastAPI() #dj

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI backend!"}