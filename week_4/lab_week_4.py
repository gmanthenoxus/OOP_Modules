class TaskList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, Task):
        self.asks.append(task)
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