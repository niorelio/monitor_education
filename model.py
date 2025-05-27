import json
import os
from dataclasses import dataclass, asdict
from typing import Dict, List


@dataclass
class Product:
    """    Класс, представляющий товар в магазине.    """
    id: int
    name: str
    price: float
    quantity: int


class ShopList:
    """
    Модель магазина, управляющая товарами и продажами,
    а также сохранением и загрузкой данных из JSON файла.
    """

    
    def __init__(self, filename='shop_data.json'):
        """
        Инициализация модели магазина.
        """
        self.filename = filename
        self.products: Dict[str, Product] = {}  # Словарь товаров, ключ — название
        self.sales: List[Dict] = []             # Список совершённых продаж
        self._next_id: int = 1                  # Счётчик для генерации уникальных id товаров
        self.load_data()                        # Загружаем данные из файла при инициализации


    def add_product(self, name: str, price: float, quantity: int):
        """
        Добавляет новый товар или обновляет существующий.
        Если товар с таким названием уже есть, увеличивает количество и обновляет цену.
        После изменения сохраняет данные.
        """
        if name in self.products:
            product = self.products[name]
            product.quantity += quantity
            product.price = price
        else:
            product = Product(id=self._next_id, name=name, price=price, quantity=quantity)
            self.products[name] = product
            self._next_id += 1
        self.save_data()

    def get_products(self) -> Dict[str, Product]:
        """    Возвращает копию словаря всех товаров.    """
        return self.products.copy()
    
    def get_product_by_id(self, product_id: int):
        """    Поиск товара по его уникальному id.    """
        for product in self.products.values():
            if product.id == product_id:
                return product
        return None

    def sell_product(self, product_id: int, quantity: int):
        product = self.get_product_by_id(product_id)
        if product is None:
            return False, None  # Товар не найден
        if product.quantity < quantity:
            return False, product.quantity  # Недостаточно товара
        product.quantity -= quantity
        total_price = product.price * quantity
        self.sales.append({
            'id': product.id,
            'name': product.name,
            'quantity': quantity,
            'total_price': total_price
        })
        self.save_data()
        return True, total_price  # Успешная продажа

    def generate_report(self):
        """    Формирует отчет о продажах.    """
        total_sales_sum = sum(sale['total_price'] for sale in self.sales)
        sales_details = self.sales.copy()
        return total_sales_sum, sales_details
    
    def save_data(self):
        """
        Сохраняет текущие данные магазина в JSON файл.
        Преобразует объекты Product в словари для записи.
        """
        products_data = {name: asdict(prod) for name, prod in self.products.items()}
        data = {
            'products': products_data,
            'sales': self.sales,
            '_next_id': self._next_id
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_data(self):
        """
        Загружает данные магазина из JSON файла, если он существует.
        Восстанавливает объекты Product из сохранённых словарей.
        """
        if not os.path.exists(self.filename):
            return
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        products_data = data.get('products', {})
        self.products = {name: Product(**prod_dict) for name, prod_dict in products_data.items()}
        self.sales = data.get('sales', [])
        self._next_id = data.get('_next_id', 1)
