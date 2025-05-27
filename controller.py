from model import Task


class TodoController:
    # Контроллер для управления задачами и взаимодействия между моделью и представлением

    def __init__(self, model, view):
        # Инициализирует контроллер
        self.model = model
        self.view = view

    def add_task(self):
        # Добавляет новую задачу в список
        description = self.view.get_new_task_description()
        task = Task(description)
        self.model.add_task(task)

    def mark_task_completed(self):
        # Отмечает задачу как выполненную.
        # Запрашивает у пользователя индекс задачи и обновляет статус задачи в модели
        index = self.view.get_task_index_to_complete()
        self.model.mark_task_completed(index)

    def remove_task(self):
        # Удаляет задачу из списка.
        # Запрашивает у пользователя индекс задачи и удаляет ее из модели
        index = self.view.get_task_index_to_remove()
        self.model.remove_task(index)

    def display_tasks(self):
        # Отображает текущий список задач с помощью представления
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)
