from model import Task


class TodoController:
    # Контроллер для управления задачами и взаимодействия между моделью и представлением


    def __init__(self, model, view):
        # Инициализирует контроллер
        self.model = model
        self.view = view

    def run(self):
        # Вызов меню
        while True:
            self.display_tasks()
            self.view.display_menu()  # Переносим вывод меню во view

            choice = input("Введите номер действия: ")

            if choice == '1':
               self.add_task()
            elif choice == '2':
                self.mark_task_completed()
            elif choice == '3':
                self.remove_task()
            elif choice == '4':
                self.view.display_exit_message()  # Переносим вывод сообщения о выходе во view
                break
            else:
                self.view.display_invalid_choice()  # Переносим вывод сообщения об ошибке во view

    def display_tasks(self):
        # Показывает список задач
        tasks = self.model.get_tasks()
        self.view.display_tasks(tasks)

    def add_task(self):
        # Добавляет новую задачу в список
        description = self.view.get_new_task_description()
        task = Task(description)
        self.model.add_task(task)
        self.model.save_tasks()  # Сохраняем изменения
   
    def mark_task_completed(self):
        # Отмечает задачу как выполненную
        try:
            index = self.view.get_task_index_to_complete()
            if index < 0 or index >= len(self.model.get_tasks()):
                self.view.display_invalid_task_number_complite()
                return
            self.model.mark_task_completed(index)
            self.model.save_tasks()  # Сохраняем изменения
        except Exception as e:
            self.view.display_error_complite(error=e)

    def remove_task(self):
        # Удаляет задачу
        try:
            index = self.view.get_task_index_to_remove()
            if index < 0 or index >= len(self.model.get_tasks()):
                self.view.display_invalid_task_number_remove()
                return
            self.model.remove_task(index)
            self.model.save_tasks()  # Сохраняем изменения
        except Exception as e:
            self.view.display_error_remove(error=e)
