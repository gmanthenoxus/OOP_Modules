# dao/task_test_dao.py

from tasklist import Task

class TaskTestDAO:
    def get_all_tasks(self):
        return [
            Task("Buy groceries", False),
            Task("Complete assignment", True),
            Task("Book doctor's appointment", False)
        ]

    def save_all_tasks(self, tasks):
        pass  # Not needed for test DAO
