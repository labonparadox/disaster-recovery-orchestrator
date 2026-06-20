from db import get_db_connection

conn = get_db_connection()

if conn:
    print("Connection successful")
    conn.close()