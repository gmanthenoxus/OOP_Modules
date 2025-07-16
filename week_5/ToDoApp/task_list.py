# tasklist.py

from users import Owner

class TaskList:
    def __init__(self, owner: Owner):
        self.tasks = []
        self.owner = owner

    def add_task(self, task: str):
        self.tasks.append(task)

    def remove_task(self, task: str):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_task(self, index: int):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        return None

    def __str__(self):
        task_list_str = "\n".join([f"{idx + 1}. {task}" for idx, task in enumerate(self.tasks)])
        return f"TaskList owned by {self.owner.name} ({self.owner.email}):\n{task_list_str if task_list_str else 'No tasks yet.'}"
