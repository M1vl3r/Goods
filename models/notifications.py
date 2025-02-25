# models/notifications.py
from config.database import get_connection

class NotificationsModel:
    @staticmethod
    def add_notification(goods_id, notif_type, message):
        conn = get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO notifications (goods_id, type, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (goods_id, notif_type, message))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_all_notifications():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notifications")
        notifications = cursor.fetchall()
        cursor.close()
        conn.close()
        return notifications
