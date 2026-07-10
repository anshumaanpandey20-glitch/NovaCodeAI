from pathlib import Path

import pymysql

from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


_database_ready = False


def _quote_identifier(identifier):
    return "`" + identifier.replace("`", "``") + "`"


def _schema_statements():
    schema_path = Path(__file__).with_name("schema.sql")
    schema_sql = schema_path.read_text(encoding="utf-8")
    cleaned_lines = [
        line
        for line in schema_sql.splitlines()
        if line.strip() and not line.strip().startswith("--")
    ]
    cleaned_sql = "\n".join(cleaned_lines)
    return [
        statement.strip()
        for statement in cleaned_sql.split(";")
        if statement.strip()
    ]


def initialize_database():
    global _database_ready

    if _database_ready:
        return

    server_connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )

    try:
        with server_connection.cursor() as cursor:
            cursor.execute(
                f"CREATE DATABASE IF NOT EXISTS {_quote_identifier(DB_NAME)} "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
            )
            cursor.execute(f"USE {_quote_identifier(DB_NAME)}")

            for statement in _schema_statements():
                print("\nExecuting SQL:")
                print(statement)
                try:
                    cursor.execute(statement)
                    print("✅ Success")
                except Exception as e:
                    print("❌ Failed:", e)
                    raise

        _database_ready = True
    finally:
        server_connection.close()


def get_db_connection():
    initialize_database()
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


class LazyConnection:
    def __init__(self):
        self._connection = None

    def _get_connection(self):
        if self._connection is None or not self._connection.open:
            self._connection = get_db_connection()
        return self._connection

    def cursor(self, *args, **kwargs):
        return self._get_connection().cursor(*args, **kwargs)

    def commit(self):
        return self._get_connection().commit()

    def close(self):
        if self._connection and self._connection.open:
            self._connection.close()


connection = LazyConnection()
