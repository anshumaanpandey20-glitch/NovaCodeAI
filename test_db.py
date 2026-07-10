from app import get_db_connection

try:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT DATABASE();")
    print("Current Database:")
    print(cursor.fetchone())

    cursor.execute("SHOW TABLES;")
    print("\nTables:")
    print(cursor.fetchall())

    cursor.execute("SHOW CREATE TABLE users;")
    print("\nUsers Table:")
    print(cursor.fetchone())

    cursor.close()
    conn.close()

except Exception as e:
    print(e)