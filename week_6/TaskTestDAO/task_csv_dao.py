# dao/task_csv_dao.py

import csv
from tasklist import Task

class TaskCsvDAO:
    def __init__(self, filename):
        self.filename = filename

    def save_all_tasks(self, tasks):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for task in tasks:
                writer.writerow([task.title, task.completed])

    def get_all_tasks(self):
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    title, completed = row
                    tasks.append(Task(title, completed == "True"))
        except FileNotFoundError:
            pass
        return tasks
