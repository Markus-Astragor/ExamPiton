# Маркіян Косик:
# Організатор завдань з використанням декораторів
# Розробіть систему організації завдань, 
# де кожне завдання має певний пріоритет. Використайте декоратори для присвоєння пріоритетів завданням. 
# Створіть функції для виведення списку завдань, впорядкованих за пріоритетом, та виконання завдань відповідно до пріоритету.


class Task:
    def __init__(self, name, priority=0):
        self.name = name
        self.priority = priority

def prioritize(priority):
    def decorator(func):
        def wrapper(*args, **kwargs):
            task = func(*args, **kwargs)
            task.priority = priority
            return task
        return wrapper
    return decorator

class TaskManagerMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class TaskManager(metaclass=TaskManagerMeta):
    def __init__(self):
        self.tasks = []

    @prioritize(priority=0)
    def create_task(self, name, priority):
        return Task(name, priority)

    def add_task(self, task):
        self.tasks.append(task)

    def get_sorted_tasks(self):
        return sorted(self.tasks, key=lambda x: x.priority)
    
    def print_tasks(self, tasks):
        for task in tasks:
            print(f"Завдання: {task.name}, Пріоритет: {task.priority}")


task_manager = TaskManager()

task_manager.add_task(task_manager.create_task("Завдання 1", 1))
task_manager.add_task(task_manager.create_task("Завдання 2", 2))
task_manager.add_task(task_manager.create_task("Завдання 3", 3))

sorted_tasks = task_manager.get_sorted_tasks()
task_manager.print_tasks(sorted_tasks)
