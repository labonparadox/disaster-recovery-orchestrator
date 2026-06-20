<<<<<<< HEAD:backend/services/signup_service.py
from database.db import get_db_connection

def signup_user(user):

    conn = get_db_connection()
=======
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
>>>>>>> 513060e7093b1ad5fa1a7270412e112d83b96b31:backend/functions/signup_service.py

    cursor = conn.cursor(dictionary=True)

    # Check if email already exists

    query = "SELECT * FROM users WHERE email = %s"

    cursor.execute(query, (user.email,))

    existing_user = cursor.fetchone()

    if existing_user:

        cursor.close()

        conn.close()

        return {
            "message": "Email already exists"
        }

    # Insert new user

    insert_query = """
    INSERT INTO users(name, email, password)
    VALUES(%s, %s, %s)
    """

    values = (
        user.name,
        user.email,
        user.password
    )

    cursor.execute(insert_query, values)

    conn.commit()

    cursor.close()

    conn.close()

    return {
        "message": "Signup Successful"
    }