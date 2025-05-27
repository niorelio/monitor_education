from model import TodoList
from view import TodoView
from controller import TodoController


if __name__ == "__main__":
    todolist = TodoList()
    todoview = TodoView()
    todocontroller = TodoController(todolist, todoview)
    todocontroller.run()