from backend.helpers.set_logger import LoggerFactory
from backend.helpers.config import settings
import logging

logger = LoggerFactory.get_logger(
    name="signup_service",
    log_file=settings.Log_file_signup,
    level=logging.INFO
)

users = []

def signup_user(user):

    logger.info(
        f"req arrive for login {user}"
    )

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