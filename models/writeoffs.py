# models/writeoffs.py
from config.database import get_connection

class WriteOffsModel:
    @staticmethod
    def add_writeoff(datetime, status, compound, count):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO writeoffs (datetime, status, compound, count) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (datetime, status, compound, count))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_writeoffs():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM writeoffs")
        writeoffs = cursor.fetchall()
        cursor.close()
        conn.close()
        return writeoffs
