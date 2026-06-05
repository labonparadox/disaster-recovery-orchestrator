from fastapi import APIRouter
from pydantic import BaseModel
from backend.functions.login_service import login_user

router = APIRouter()

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(user: UserLogin):

    return login_user(user)