# models/goods.py
from config.database import get_connection

class GoodsModel:
    @staticmethod
    def add_goods(writeOffs_id, deliveries_id, name, description, price, count):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO goods (writeOffs_id, deliveries_id, name, description, price, count)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (writeOffs_id, deliveries_id, name, description, price, count))
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def get_goods_stock():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT name, count FROM goods")
        goods = cursor.fetchall()
        cursor.close()
        conn.close()
        return goods

    @staticmethod
    def get_low_stock_goods(threshold=10):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT name, count FROM goods WHERE count <= %s", (threshold,))
        goods = cursor.fetchall()
        cursor.close()
        conn.close()
        return goods
