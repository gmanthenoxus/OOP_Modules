# tasklist.py

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def __str__(self):
        return f"[{'x' if self.completed else ' '}] {self.title}"

class RecurringTask(Task):
    def __init__(self, title, completed=False, interval=None):
        super().__init__(title, completed)
        self.interval = interval

    def __str__(self):
        return super().__str__() + f" (Recurring every {self.interval})"

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def check_task_index(self, index):
        return 0 <= index < len(self.tasks)

    @property
    def uncompleted_tasks(self):
        return [task for task in self.tasks if not task.completed]
