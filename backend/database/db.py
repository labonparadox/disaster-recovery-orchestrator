import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

def get_db_connection():

    try:

        connection = mysql.connector.connect(

            host=os.getenv("DB_HOST"),

            user=os.getenv("DB_USER"),

            password=os.getenv("DB_PASSWORD"),

            database=os.getenv("DB_NAME"),

            port=int(os.getenv("DB_PORT"))

        )

        print("Database connected successfully")

        return connection

    except Exception as e:

        print("Database connection failed")

        print(e)