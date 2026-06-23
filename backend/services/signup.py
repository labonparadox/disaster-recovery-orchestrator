from fastapi import APIRouter
from pydantic import BaseModel
from functions.signup_service import signup_user

router = APIRouter()


class UserSignup(BaseModel):
    name: str
    email: str
    password: str
    image: str
    port: int
    health_point: str


@router.post("/signup")
def signup(user: UserSignup):

    return signup_user(user)
