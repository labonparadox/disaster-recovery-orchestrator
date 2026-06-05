from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

users = []

class UserSignup(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


@router.post("/signup")
def signup(user: UserSignup):

    for existing_user in users:

        if existing_user["email"] == user.email:
            return {
                "message": "Email already exists"
            }

    users.append({
        "name": user.name,
        "email": user.email,
        "password": user.password
    })

    return {
        "message": "Signup Successful"
    }


@router.post("/login")
def login(user: UserLogin):

    for existing_user in users:

        if (
            existing_user["email"] == user.email
            and existing_user["password"] == user.password
        ):
            return {
                "message": "Login Successful"
            }

    return {
        "message": "Invalid Credentials"
    }