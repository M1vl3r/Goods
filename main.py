# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from controllers.deliveries_controller import DeliveriesController
from controllers.writeoffs_controller import WriteOffsController
from controllers.goods_controller import GoodsController


class GoodsManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Управление товарами")
        self.geometry("600x500")
        self.create_widgets()

    def create_widgets(self):
        tab_control = ttk.Notebook(self)

        # Вкладки
        self.delivery_tab = ttk.Frame(tab_control)
        self.writeoff_tab = ttk.Frame(tab_control)
        self.stock_tab = ttk.Frame(tab_control)
        self.low_stock_tab = ttk.Frame(tab_control)

        tab_control.add(self.delivery_tab, text='Добавить поступление')
        tab_control.add(self.writeoff_tab, text='Добавить списание')
        tab_control.add(self.stock_tab, text='Остатки на складе')
        tab_control.add(self.low_stock_tab, text='Товары для пополнения')

        tab_control.pack(expand=1, fill="both")

        self.create_delivery_tab()
        self.create_writeoff_tab()
        self.create_stock_tab()
        self.create_low_stock_tab()

    # Добавление поступления товара
    def create_delivery_tab(self):
        ttk.Label(self.delivery_tab, text="Дата и время (ГГГГ-ММ-ДД ЧЧ:ММ:СС):").pack(pady=5)
        self.delivery_datetime = ttk.Entry(self.delivery_tab)
        self.delivery_datetime.pack(pady=5)

        ttk.Label(self.delivery_tab, text="Статус:").pack(pady=5)
        self.delivery_status = ttk.Entry(self.delivery_tab)
        self.delivery_status.pack(pady=5)

        ttk.Label(self.delivery_tab, text="Состав:").pack(pady=5)
        self.delivery_compound = ttk.Entry(self.delivery_tab)
        self.delivery_compound.pack(pady=5)

        ttk.Label(self.delivery_tab, text="Количество:").pack(pady=5)
        self.delivery_count = ttk.Entry(self.delivery_tab)
        self.delivery_count.pack(pady=5)

        ttk.Label(self.delivery_tab, text="Название товара:").pack(pady=5)
        self.delivery_name = ttk.Entry(self.delivery_tab)
        self.delivery_name.pack(pady=5)

        ttk.Label(self.delivery_tab, text="Описание:").pack(pady=5)
        self.delivery_description = ttk.Entry(self.delivery_tab)
        self.delivery_description.pack(pady=5)

        ttk.Label(self.delivery_tab, text="Цена:").pack(pady=5)
        self.delivery_price = ttk.Entry(self.delivery_tab)
        self.delivery_price.pack(pady=5)

        ttk.Button(self.delivery_tab, text="Добавить поступление", command=self.add_delivery).pack(pady=10)

    def add_delivery(self):
        try:
            DeliveriesController.add_delivery(
                self.delivery_datetime.get(),
                self.delivery_status.get(),
                self.delivery_compound.get(),
                int(self.delivery_count.get()),
                self.delivery_name.get(),
                self.delivery_description.get(),
                int(self.delivery_price.get())
            )
            messagebox.showinfo("Успех", "Поступление добавлено.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось добавить поступление: {e}")

    # Добавление списания товара
    def create_writeoff_tab(self):
        ttk.Label(self.writeoff_tab, text="Дата и время (ГГГГ-ММ-ДД ЧЧ:ММ:СС):").pack(pady=5)
        self.writeoff_datetime = ttk.Entry(self.writeoff_tab)
        self.writeoff_datetime.pack(pady=5)

        ttk.Label(self.writeoff_tab, text="Статус:").pack(pady=5)
        self.writeoff_status = ttk.Entry(self.writeoff_tab)
        self.writeoff_status.pack(pady=5)

        ttk.Label(self.writeoff_tab, text="Состав:").pack(pady=5)
        self.writeoff_compound = ttk.Entry(self.writeoff_tab)
        self.writeoff_compound.pack(pady=5)

        ttk.Label(self.writeoff_tab, text="Количество:").pack(pady=5)
        self.writeoff_count = ttk.Entry(self.writeoff_tab)
        self.writeoff_count.pack(pady=5)

        ttk.Label(self.writeoff_tab, text="ID товара:").pack(pady=5)
        self.writeoff_goods_id = ttk.Entry(self.writeoff_tab)
        self.writeoff_goods_id.pack(pady=5)

        ttk.Button(self.writeoff_tab, text="Добавить списание", command=self.add_writeoff).pack(pady=10)

    def add_writeoff(self):
        try:
            WriteOffsController.add_writeoff(
                self.writeoff_datetime.get(),
                self.writeoff_status.get(),
                self.writeoff_compound.get(),
                int(self.writeoff_count.get()),
                int(self.writeoff_goods_id.get())
            )
            messagebox.showinfo("Успех", "Списание добавлено.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось добавить списание: {e}")

    # Показ остатков на складе
    def create_stock_tab(self):
        ttk.Button(self.stock_tab, text="Показать остатки", command=self.show_stock).pack(pady=10)
        self.stock_list = tk.Text(self.stock_tab, height=15, width=70)
        self.stock_list.pack(pady=5)

    def show_stock(self):
        self.stock_list.delete(1.0, tk.END)
        goods = GoodsController.show_goods_stock()
        for item in goods:
            self.stock_list.insert(tk.END, f"{item['name']} - {item['count']} шт.\n")

    # Показ товаров для пополнения
    def create_low_stock_tab(self):
        ttk.Label(self.low_stock_tab, text="Минимальный остаток:").pack(pady=5)
        self.low_stock_threshold = ttk.Entry(self.low_stock_tab)
        self.low_stock_threshold.insert(0, "10")
        self.low_stock_threshold.pack(pady=5)

        ttk.Button(self.low_stock_tab, text="Показать товары для пополнения", command=self.show_low_stock).pack(pady=10)
        self.low_stock_list = tk.Text(self.low_stock_tab, height=15, width=70)
        self.low_stock_list.pack(pady=5)

    def show_low_stock(self):
        self.low_stock_list.delete(1.0, tk.END)
        threshold = int(self.low_stock_threshold.get())
        goods = GoodsController.show_low_stock(threshold)
        for item in goods:
            self.low_stock_list.insert(tk.END, f"{item['name']} - {item['count']} шт.\n")


if __name__ == "__main__":
    app = GoodsManagementApp()
    app.mainloop()
