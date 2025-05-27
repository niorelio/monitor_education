from tabulate import tabulate


class TodoView:
    # Класс для отображения задач и взаимодействия с пользователем

    def display_tasks(self, tasks):
        # Отображает список задач в виде таблицы
        table = [[index + 1, task.description, "v" if task.completed else "x"] for index, task in enumerate(tasks)]
        print("\nСписок задач:")
        print(tabulate(table, headers=["№", "Описание", "Статус"], tablefmt="grid"))

    def get_new_task_description(self):
        # Запрашивает у пользователя описание новой задачи
        return input("Введите описание новой задачи: ")

    def get_task_index_to_complete(self):
        # Запрашивает у пользователя номер задачи для отметки как выполненной
        return int(input("Введите номер задачи для отметки как выполненной: ")) - 1

    def get_task_index_to_remove(self):
        # Запрашивает у пользователя номер задачи для удаления
        return int(input("Введите номер задачи для удаления: ")) - 1
