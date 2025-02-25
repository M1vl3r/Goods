# controllers/notifications_controller.py
from models.notifications import NotificationsModel

class NotificationsController:
    @staticmethod
    def add_notification(goods_id, notif_type, message):
        NotificationsModel.add_notification(goods_id, notif_type, message)

    @staticmethod
    def get_notifications():
        return NotificationsModel.get_all_notifications()
