from fastapi import FastAPI
from backend.services.login import router as login
from backend.services.signup import router as signup
from backend.health.health import router as health
app = FastAPI()


app.include_router(login)
app.include_router(signup)
app.include_router(health)

@app.get("/")
def home():
    return {"message": "Disaster Recovery API Running"}