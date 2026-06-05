from backend.functions.signup_service import users
from backend.helpers.set_logger import LoggerFactory
from backend.helpers.config import settings
import logging

logger = LoggerFactory.get_logger(
    name="login_service",
    log_file=settings.Log_file_login,
    level=logging.INFO
)



def login_user(user):

    for existing_user in users:

        logger.info(
            f"req arrive for login {user}"
        )

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