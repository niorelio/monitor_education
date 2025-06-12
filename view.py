import tabulate as tl
from model import ShopList


class ShopView:
    """
    Класс-представление для отображения информации пользователю.
    Обрабатывает вывод списка товаров, сообщений и отчетов.
    """


    def get_menu_item(self) -> int:
        # вывод меню
        print("Выберите действие:")
        print("1. Показать список товаров")
        print("2. Добавить новый товар")
        print("3. Продать товар")
        print("4. Показать отчет о продажах")
        print("5. Выход")

        try:
            return int(input("Введите номер пункта меню: "))
        
        except ValueError:
            return -1

    def show_products(self, products):
        # вывод списка товаров

        if not products:
            print("Товаров в магазине пока нет.")
            return
        # Подготовка данных для табличного отображения
        table_data = [
            [product.id, product.name, product.price, product.quantity]
            for product in products.values()
        ]
        headers = ["ID", "Название", "Цена", "Количество"]
        print(tl.tabulate(table_data, headers=headers, tablefmt="grid"))

    def ask_for_new_product(self):
        name = input("Введите название товара: ").strip()

        if name == '':
            return None  # Если название пустое, возвращаем None
        price = None

        while price is None:
            price = self.ask_for_price()  # Используем метод для ввода цены

            if price is None:
                print("Некорректный ввод цены. Пожалуйста, введите число.")  # Сообщение об ошибке
        quantity = None

        while quantity is None:
            quantity = self.ask_for_quantity()  # Используем метод для ввода количества

            if quantity is None:
                print("Некорректный ввод количества. Пожалуйста, введите положительное число.")  # Сообщение об ошибке
        return name, price, quantity

    def ask_for_price(self):

        while True:
            price_input = input("Введите цену товара: ")
            price_input = price_input.replace(',', '.')  # Заменяем запятую на точку

            try:
                return float(price_input)  # Преобразуем в число с плавающей запятой
            
            except ValueError:
                print("Некорректный ввод цены. Пожалуйста, введите число.")  # Сообщение об ошибке

    def ask_for_quantity(self):

        while True:
            quantity_input = input("Введите количество товара: ")

            try:
                quantity = int(quantity_input)

                if quantity < 0:
                    print("Количество должно быть положительным числом.")  # Сообщение об ошибке
                    continue  # Повторяем ввод
                return quantity
            
            except ValueError:
                print("Некорректный ввод количества. Пожалуйста, введите число.")  # Сообщение об ошибке

    def prompt_product_id(self):

        while True:

            try:
                return int(input("Введите ID товара для продажи: "))
            
            except ValueError:
                print("Некорректный ввод ID товара. Пожалуйста, введите число.")

    def ask_for_sale_quantity(self):

        while True:

            try:
                quantity = int(input("Введите количество товара для продажи: "))

                if quantity <= 0:
                    print("Количество должно быть положительным числом.")
                    continue  # Повторяем ввод
                return quantity
            
            except ValueError:
                print("Некорректный ввод количества. Пожалуйста, введите число.")

    def display_sale_message(self, success, result):
        # продажа товара

        if success:
            print(f"Продажа успешно проведена. Сумма: {result:.2f}")

        else:

            if result is None:
                print("Ошибка продажи: Товар с таким ID не найден.")

            else:
                print(f"Ошибка продажи: Недостаточно товара. Доступно: {result}.")

    def display_sales_report(self, total_sales_sum, sales):
        # отчет о продажах

        if not sales:
            print("Продаж ещё не было.")

        else:
            # Подготовка данных для табличного отображения
            table_data = [
                [sale['id'], sale['name'], sale['quantity'], sale['total_price']]
                for sale in sales
            ]
            headers = ["ID", "Название", "Количество", "Сумма"]
            print(tl.tabulate(table_data, headers=headers, tablefmt="grid"))
    
        # Выделяем сообщение о общей сумме продаж
        print("\n" + "*" * 40)  # Разделительная линия
        print(f"Общая сумма продаж: {total_sales_sum:.2f}")
        print("*" * 40 + "\n")  # Разделительная линия

    def display_exit_message(self):
        print("Спасибо за использование магазина. До свидания!")

    def display_invalid_choice(self):
        print("Выбран неверный пункт меню. Пожалуйста, попробуйте снова.")
