# controllers/task_manager_controller.py

class TaskManagerController:
    def __init__(self, task_list):
        self.task_list = task_list

    def add_task(self, title):
        from factory.task_factory import TaskFactory
        task = TaskFactory.create_task(title)
        self.task_list.add_task(task)

    def complete_task(self, index):
        if self.task_list.check_task_index(index):
            self.task_list.complete_task(index)
        else:
            print("Task index does not exist.")

    def view_tasks(self):
        for i, task in enumerate(self.task_list.uncompleted_tasks, 1):
            print(f"{i}. {task}")
