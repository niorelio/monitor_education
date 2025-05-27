from model import ShopList
from view import ShopView


class ShopController:
    """
    Контроллер, обрабатывающий пользовательский ввод,
    взаимодействующий с моделью и представлением.
    """

    def __init__(self, model, view):
        """    Инициализация контроллера.    """
        self.model = model
        self.view = view

    def run(self):
        while True:
            choice = self.view.get_menu_item()
            
            if choice == 1:
                products = self.model.get_products()
                self.view.show_products(products)
            
            elif choice == 2:
                data = self.view.ask_for_new_product()
                if data is None:  # Если данные некорректные, обработка происходит во view
                    continue  # Возвращаемся к началу цикла
                name, price, quantity = data
                self.model.add_product(name, price, quantity)
            
            elif choice == 3:
                while True:
                    product_id = self.view.prompt_product_id()  # Запрашиваем ID товара
                    if product_id is None:
                        continue  # Некорректный ID, повторяем ввод

                    product = self.model.get_product_by_id(product_id)  # Получаем товар по ID
                    if product is None:
                        self.view.display_sale_message(False, None)  # Товар не найден
                        continue  # Повторяем ввод ID товара

                    quantity = self.view.ask_for_quantity()  # Запрашиваем количество
                    if quantity is None:
                        continue  # Некорректное количество, повторяем ввод

                    success, result = self.model.sell_product(product_id, quantity)  # Пытаемся продать товар
                    self.view.display_sale_message(success, result)  # Отображаем результат продажи
                    if success:
                        break  # Если продажа успешна, выходим из цикла

            elif choice == 4:
                total_sales_sum, sales = self.model.generate_report()
                self.view.display_sales_report(total_sales_sum, sales)
            
            elif choice == 5:
                self.view.display_exit_message()
                break
            
            else:
                self.view.display_invalid_choice()
