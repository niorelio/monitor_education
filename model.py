import json
import os


class Task:
    # Класс, представляющий задачу

    def __init__(self, description):
        # Инициализирует новую задачу
        self.description = description
        self.completed = False

    def mark_completed(self):
        # Отмечает задачу как выполненную
        self.completed = True

    def __str__(self):
        # Возвращает строку с описанием задачи и ее статусом (выполнена или нет)
        status = "v" if self.completed else "x"
        return f"[{status}] {self.description}"


class TodoList:
    # Класс, представляющий список задач

    def __init__(self, filename='tasks.json'):
        # Инициализирует новый список задач
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task):
        # Добавляет новую задачу в список
        self.tasks.append(task)

    def mark_task_completed(self, index):
        # Отмечает задачу как выполненную по индексу
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()

    def remove_task(self, index):
        # Удаляет задачу из списка по индексу
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def get_tasks(self):
        # Возвращает список всех задач
        return self.tasks

    def save_tasks(self):
        # Сохраняет список задач в файл в формате JSON
        with open(self.filename, 'w') as f:
            json.dump([{'description': task.description, 'completed': task.completed} for task in self.tasks], f)

    def load_tasks(self):
        # Загружает список задач из файла, если он существует
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    tasks_data = json.load(f)
                    self.tasks = [Task(task['description']) for task in tasks_data]
                    for index, task in enumerate(tasks_data):
                        if task.get('completed', False):
                            self.tasks[index].mark_completed()
            except (json.JSONDecodeError, TypeError) as e:
                print(f"Ошибка при загрузке задач: {e}. Файл может быть поврежден.")
                self.tasks = []
