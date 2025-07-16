# factory/task_factory.py

from tasklist import Task, RecurringTask

class TaskFactory:
    @staticmethod
    def create_task(title, interval=None):
        if interval:
            return RecurringTask(title, interval=interval)
        return Task(title)
