class TaskList:
    def __init__(self, owner):
        self.owner = owner.title()
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added")
    
    def remove_task(self, ix: int):
        if ix in self.tasks:
            self.tasks.remove(ix)
            print("Task removed")
        else:
            print("Task not found")
    
    def view_tasks(self):
        for task in self.tasks:
            print(task)
    
    def list_options(self):
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Exit")

class Task:
    def __init__(self, description, due_date, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed