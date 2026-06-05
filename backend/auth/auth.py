from fastapi import APIRouter
from pydantic import BaseModel

from services.signup_service import signup_user
from services.login_service import login_user

router = APIRouter()


class UserSignup(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


@router.post("/signup")
def signup(user: UserSignup):

    return signup_user(user)


@router.post("/login")
def login(user: UserLogin):

    return login_user(user)