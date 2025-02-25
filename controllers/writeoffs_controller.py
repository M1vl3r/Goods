# controllers/writeoffs_controller.py
from models.writeoffs import WriteOffsModel
from models.goods import GoodsModel
from models.notifications import NotificationsModel

class WriteOffsController:
    @staticmethod
    def add_writeoff(datetime, status, compound, count, goods_id):
        WriteOffsModel.add_writeoff(datetime, status, compound, count)
        goods = GoodsModel.get_goods_stock()
        item = next((g for g in goods if g['name'] == compound), None)

        if item:
            new_count = item['count'] - count
            if new_count < 0:
                new_count = 0
            # Обновление количества товара
            GoodsModel.add_goods(writeOffs_id=0, deliveries_id=0, name=compound, description="", price=0, count=new_count)
            NotificationsModel.add_notification(goods_id, "Списание", f"Списано {count} единиц {compound}")
