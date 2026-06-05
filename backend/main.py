from fastapi import FastAPI
from auth.auth import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Disaster Recovery API Running"}