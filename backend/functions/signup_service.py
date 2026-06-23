from database.db import get_db_connection

def signup_user(user):

    conn = get_db_connection()

    cursor = conn.cursor()

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


    insert_query = """
    INSERT INTO users(name, email, password, docker_image, port , health_point)
    VALUES(%s, %s, %s,%s,%s,%s)
    """

    values = (
        user.name,
        user.email,
        user.password,
        user.image,
        user.port,
        user.health_point
    )

    cursor.execute(insert_query, values)

    conn.commit()

    cursor.close()

    conn.close()

    return {
        "message": "Signup Successful"
    }