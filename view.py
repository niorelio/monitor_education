from tabulate import tabulate


class TodoView:
    # Класс для отображения задач и взаимодействия с пользователем


    def display_menu(self):
        # Отображает меню
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Удалить задачу")
        print("4. Выход")

    def display_exit_message(self):
        # Сообщение при закрытии программы
        print("Сохранено. Выход из программы.")

    def display_invalid_choice(self):
        # Ошибка выбора задачи
        print("Неверный выбор. Пожалуйста, попробуйте снова.")

    def display_invalid_task_number_complite(self):
        # Ошибка номера задачи при отметке выполнения
        print("Неверный номер задачи.")

    def display_error_complite(self, error=None):
        # Ошибка при отметке задачи
        if error:
            print(f"Ошибка при отметке задачи: {error}")
        else:
            print("Произошла ошибка.")

    def display_invalid_task_number_remove(self):
        # Ошибка номера задачи при удалении
        print("Неверный номер задачи.")

    def display_error_remove(self, error=None):
        # Ошибка при удалении задачи
        if error:
            print(f"Ошибка при удалении задачи: {error}")
        else:
            print("Произошла ошибка.")

    def display_tasks(self, tasks):
        # Отображает список задач в виде таблицы
        table = [[index + 1, task.description, "v" if task.completed else "x"] for index, task in enumerate(tasks)]
        print("\nСписок задач:")
        print(tabulate(table, headers=["№", "Описание", "Статус"], tablefmt="grid"))

    def get_new_task_description(self):
        # Запрашивает у пользователя описание новой задачи
        while True:
            description = input("Введите описание новой задачи: ")
            if description.strip():
                return description
            print("Описание задачи не может быть пустым. Пожалуйста, введите корректное описание.")

    def get_task_index_to_complete(self):
        # Запрашивает у пользователя номер задачи для отметки как выполненной
        while True:
            try:
                index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
                return index
            except ValueError:
                print("Пожалуйста, введите корректный номер задачи.")
                
    def get_task_index_to_remove(self):
        # Запрашивает у пользователя номер задачи для удаления
        while True:
            try:
                index = int(input("Введите номер задачи для удаления: ")) - 1
                return index
            except ValueError:
                print("Пожалуйста, введите корректный номер задачи.")