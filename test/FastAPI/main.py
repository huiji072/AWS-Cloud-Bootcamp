from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "reload test"}

@app.post("/hello")
async def hello():
    return {"message" : "post test"}

