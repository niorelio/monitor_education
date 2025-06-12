import json
import os
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional


@dataclass


class Product:
    """Класс, представляющий товар в магазине."""
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
        self.products: Dict[int, Product] = {}
        self.sales: List[Dict] = []
        self._next_id: int = 1
        self.load_data()

    def add_product(self, name: str, price: float, quantity: int):
        """
        Добавляет новый товар с уникальным id.
        Если товар с таким названием и ценой уже существует, увеличивает его количество.
        """
            
        # Проверяем, существует ли товар с таким названием и ценой
        for product in self.products.values():
            
            if product.name == name and product.price == price:
                product.quantity += quantity  # Увеличиваем количество
                self.save_data()
                return
        # Если товар не найден, создаем новый
        product = Product(id=self._next_id, name=name, price=price, quantity=quantity)
        self.products[self._next_id] = product
        self._next_id += 1
        self.save_data()

    def get_products(self) -> Dict[int, Product]:
        """
        Возвращает копию словаря всех товаров.
        """
        return self.products.copy()
    
    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        """Поиск товара по его уникальному id."""
        return self.products.get(product_id, None)

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
        """Формирует отчёт о продажах."""
        total_sales_sum = sum(sale['total_price'] for sale in self.sales)
        sales_details = self.sales.copy()
        return total_sales_sum, sales_details

    def save_data(self):
        """
        Сохраняет данные с ключом по id (числу, приведённому к строке).
        """
        products_data = {str(pid): asdict(prod) for pid, prod in self.products.items()}
        data = {
            'products': products_data,
            'sales': self.sales,
            '_next_id': self._next_id
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_data(self):
       
       if not os.path.exists(self.filename):
           return
       
       with open(self.filename, 'r', encoding='utf-8') as f:
           data = json.load(f)
       products_data = data.get('products', {})
       self.products = {}

       for pid_str, prod_dict in products_data.items():
           
           try:
               pid = int(pid_str)
               self.products[pid] = Product(**prod_dict)

           except (ValueError, TypeError):
               continue
       self.sales = data.get('sales', [])
       self._next_id = max(self.products.keys(), default=0) + 1

    def debug_print_products(self):

        if not self.products:
            print("  Товаров нет.")

        for pid, product in self.products.items():
            print(f"  ID: {pid}, Название: {product.name}, Цена: {product.price}, Количество: {product.quantity}")
