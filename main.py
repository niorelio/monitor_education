from model import TodoList
from view import TodoView
from controller import TodoController


def main():
    # Основная функция для управления приложением Todo List

    # Инициализация объектов для работы с задачами, представлением и контроллером
    todo_list = TodoList()  # Создаем экземпляр списка задач
    todo_view = TodoView()  # Создаем экземпляр представления задач
    todo_controller = TodoController(todo_list, todo_view)  # Создаем контроллер, связывающий список задач и представление
    while True:
        # Отображаем текущий список задач
        todo_controller.display_tasks()

        # Выводим меню действий для пользователя
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Удалить задачу")
        print("4. Выход")

        # Получаем выбор пользователя
        choice = input("Введите номер действия: ")

        # Обрабатываем выбор пользователя
        if choice == '1':
            todo_controller.add_task()  # Добавляем новую задачу
            todo_list.save_tasks()  # Сохраняем изменения после добавления
        elif choice == '2':
            todo_controller.mark_task_completed()  # Отмечаем задачу как выполненную
            todo_list.save_tasks()  # Сохраняем изменения после изменения задачи
        elif choice == '3':
            todo_controller.remove_task()  # Удаляем задачу
            todo_list.save_tasks()  # Сохраняем изменения после удаления
        elif choice == '4':
            todo_list.save_tasks()  # Сохраняем перед выходом
            print("Сохранено. Выход из программы.")
            break  # Выходим из цикла и завершаем программу
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")  # Обработка неверного выбора


if __name__ == "__main__":
    main()  # Запускаем основную функцию при выполнении скрипта
