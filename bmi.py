# создаем класс и объекты
class BMICalculator:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.bmi = self.calculate_bmi()
        self.category = self.determine_category()
# считаем ИМТ
    def calculate_bmi(self):
        return round(self.weight / (self.height / 100) ** 2, 2)
# определяем категорию
    def determine_category(self):
        if self.bmi <= 18.5:
            return "Недостаточная масса тела"
        elif self.bmi <= 24.9:
            return "Норма"
        elif self.bmi <= 29.9:
            return "Избыточная масса тела"
        else:
            return "Ожирение"
# задаем рекомендации
    def get_recommendation(self, choice):
        recommendations = {
            1: "Надо больше есть",
            2: "Так держать",
            3: "Надо больше двигаться",
        }
        return recommendations.get(
            choice, "Неверный выбор. Пожалуйста, выберите число от 1 до 3."
        )
# проверяем на ошибку ввод метрик
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите числовое значение.")
# проверяем на ошибку ввод рекомендаций
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")


# запрашиваем данные
height = get_float_input("Введите рост в сантиметрах: ")
weight = get_float_input("Введите вес в килограммах: ")

# создаем экземляр класса
bmi_calculator = BMICalculator(height, weight)

# форматируем вывод
print(
    f"Индекс массы тела равен {bmi_calculator.bmi:.2f} - это {bmi_calculator.category}"
)

# запрашиваем рекомендации
print("Выберите число от 1 до 3 для получения рекомендации:")
print("1. Для недостаточной массы тела")
print("2. Для нормы")
print("3. Для избыточной массы тела или ожирения")

# проверяем на ошибку рекомендации
while True:
    choice = get_int_input("Ваш выбор: ")
    if choice in [1, 2, 3]:
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите число от 1 до 3.")

# получаем результат
recommendation = bmi_calculator.get_recommendation(choice)
print(recommendation)
