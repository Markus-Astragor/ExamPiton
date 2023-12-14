# Маркіян Косик:
# Організатор завдань з використанням декораторів
# Розробіть систему організації завдань, 
# де кожне завдання має певний пріоритет. Використайте декоратори для присвоєння пріоритетів завданням. 
# Створіть функції для виведення списку завдань, впорядкованих за пріоритетом, та виконання завдань відповідно до пріоритету.
import uuid
import re

class Task:
    def __init__(self, name, priority=0, id=0):
        self.name = name
        self.priority = priority
        self.id = id

def prioritize(func):
    def wrapper(*args, **kwargs):
        task = func(*args, **kwargs)
        return task
    return wrapper
    

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

    @prioritize
    def create_task(self, name, priority, id):
        return Task(name, priority, id)

    def add_task(self, task):
        self.tasks.append(task)

    def get_sorted_tasks(self):
        return sorted(self.tasks, key=lambda x: x.priority)
    
    def print_tasks(self):
        for task in self.tasks:
            print(f"Task: {task.name}, Priority: {task.priority}, id:{task.id}")

    def find_task_by_id(self, id):
        success = False
        for task in self.tasks:
            if re.sub(r'urn:uuid:', '', task.id.urn) == id:
                success = True
                return task
        if not success: return 'Not task with such id'
    
    def delete_task_by_id(self, id):
        for i,task in enumerate(self.tasks):
            if re.sub(r'urn:uuid:', '', task.id.urn) == id:
                del self.tasks[i]


while True:
    task_manager = TaskManager()
    print('Hello user. Enter your answer:\n1)Create a task\n2)Read tasks\n3)Update a task\n4)Delete a task\n5)Exit')
    answer = int(input('Enter your answer\n'))
    match answer:
        case 1:
            task_text = input('Enter a text for your task\n')
            prioritization_num = int(input('Enter a number to prioritize task\n'))
            task_manager.add_task(task_manager.create_task(task_text, prioritization_num, uuid.uuid4()))
        case 2:
            sorted_tasks = task_manager.get_sorted_tasks()
            task_manager.print_tasks()
        case 3:
            answer_id = input('Enter the id of task you want to edit\n')
            needed_task = task_manager.find_task_by_id(answer_id)
            print(needed_task)
            if needed_task != 'Not task with such id': 
                print('What do you want to change?\n1)Name\n2)Priority')
                answer = int(input('Enter your answer\n'))
                match answer:
                    case 1:
                        enter_name_for_task = input('Enter text for task')
                        needed_task.name = enter_name_for_task
                        task_manager.print_tasks()
                    case 2:
                        enter_priority = int(input('Enter a number for prioritization\n'))
                        needed_task.priority = enter_priority
                        task_manager.print_tasks()
                    case _:
                        print('Enter sth normal')
        
        case 4:
            answer_id = input('Enter the id of task you want to edit\n')
            needed_task = task_manager.find_task_by_id(answer_id)
            print(needed_task)
            if needed_task != 'Not task with such id':
                task_manager.delete_task_by_id(answer_id)

        case 5:
            quit()
        case _:
            print('Enter sth normal')



