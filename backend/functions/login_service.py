from database.db import get_db_connection

def login_user(user):

    conn = get_db_connection()

    if conn is None:
        return {
        "message": "Database connection failed"
    }

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT * FROM users
    WHERE email = %s
    AND password = %s
    """

    values = (
        user.email,
        user.password
    )

    cursor.execute(query, values)

    existing_user = cursor.fetchone()

    cursor.close()

    conn.close()

    if existing_user:

        return {
            "message": "Login Successful"
        }

    return {
        "message": "Invalid Credentials"
    }