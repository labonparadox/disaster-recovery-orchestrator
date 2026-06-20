from database.db import get_db_connection

def signup_user(user):

    conn = get_db_connection()

    if conn is None:
        return {
            "message": "Database connection failed"
        }

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