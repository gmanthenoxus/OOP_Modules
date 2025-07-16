# tasklist.py

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.title}"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        print("Uncompleted Tasks:")
        for task in self.uncompleted_tasks:
            idx = self.tasks.index(task)
            print(f"{idx + 1}. {task}")

    @property
    def uncompleted_tasks(self):
        return [task for task in self.tasks if not task.completed]
