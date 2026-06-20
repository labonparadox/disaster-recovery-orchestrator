from fastapi import FastAPI
from services.login import router as login
from services.signup import router as signup
from health.health import router as health

app = FastAPI()

app.include_router(login)
app.include_router(signup)
app.include_router(health)

@app.get("/")
def home():
    return {"message": "Disaster Recovery API Running"}