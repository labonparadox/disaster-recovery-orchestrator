from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.login import router as login
from services.signup import router as signup
from health.health import router as health

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=["http://localhost:5176"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

)

app.include_router(login)
app.include_router(signup)
app.include_router(health)

@app.get("/")
def home():
    return {"message": "Disaster Recovery API Running"}