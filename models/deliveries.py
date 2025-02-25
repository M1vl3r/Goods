# models/deliveries.py
from config.database import get_connection

class DeliveriesModel:
    @staticmethod
    def add_delivery(datetime, status, compound, count):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO deliveries (datetime, status, compound, count) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (datetime, status, compound, count))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_deliveries():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM deliveries")
        deliveries = cursor.fetchall()
        cursor.close()
        conn.close()
        return deliveries
