from database.db import get_db_connection
from helpers.set_logger import LoggerFactory
from helpers.config import settings
import logging

logger = LoggerFactory.get_logger(
    name="login_service",
    log_file=settings.Log_file_login,
    level=logging.INFO
)

def login_user(user):
    logger.info(f"Login request for email: {user.email}")

    conn = get_db_connection()
    if not conn:
        return {"message": "Database connection failed"}

    cursor = conn.cursor()
    try:

        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (user.email, user.password))
        existing_user = cursor.fetchone()

        if existing_user:
            logger.info(f"Login successful for: {user.email}")
            return {
                "message": "Login Successful",
                "user": {
                    "id": existing_user[0],
                    "name": existing_user[1],
                    "email": existing_user[2]
                }
            }
        else:
            logger.warning(f"Login failed for: {user.email}")
            return {"message": "Invalid Credentials"}
    except Exception as e:
        logger.error(f"Error in login: {e}")
        return {"message": f"Error: {str(e)}"}
    finally:
        cursor.close()
        conn.close()