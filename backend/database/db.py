import mysql.connector
from backend.helpers.config import settings

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host= settings.Endpoint,
            user=settings.user,
            password=settings.password,
            database=settings.database,
            port=settings.port
        )

        print("Database connected successfully")

        return connection

    except Exception as e:
        print("Database connection failed")
        print(e)