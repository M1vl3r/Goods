# controllers/goods_controller.py
from models.goods import GoodsModel

class GoodsController:
    @staticmethod
    def show_goods_stock():
        return GoodsModel.get_goods_stock()

    @staticmethod
    def show_low_stock(threshold=10):
        return GoodsModel.get_low_stock_goods(threshold)
