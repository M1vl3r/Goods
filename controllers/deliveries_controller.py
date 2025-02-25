# controllers/deliveries_controller.py
from models.deliveries import DeliveriesModel
from models.goods import GoodsModel

class DeliveriesController:
    @staticmethod
    def add_delivery(datetime, status, compound, count, name, description, price):
        DeliveriesModel.add_delivery(datetime, status, compound, count)
        # Получаем ID последней доставки
        deliveries = DeliveriesModel.get_all_deliveries()
        last_delivery_id = deliveries[-1]['deliveries_id']
        GoodsModel.add_goods(writeOffs_id=0, deliveries_id=last_delivery_id, name=name, description=description, price=price, count=count)
