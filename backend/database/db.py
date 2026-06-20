import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="database-1.clegc42skt93.ap-south-1.rds.amazonaws.com",
            user="admin",
            password="Shruti1234",
            database="disaster_recovery",
            port=3306
        )

        print("Database connected successfully")

        return connection

    except Exception as e:
        print("Database connection failed")
        print(e)