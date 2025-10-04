"""
Task Test DAO Module - Week 6 Data Persistence

Demonstrates DAO (Data Access Object) pattern implementation:
- In-memory storage for testing purposes
- CRUD operations abstraction
- Interface consistency for different storage backends
- UML class diagram implementation (TaskTestDAO)

Author: [MOSES GANA]
"""

import datetime
from task import Task, RecurringTask


class TaskTestDAO:
    """Test Data Access Object providing hardcoded test data."""

    def __init__(self, storage_path: str = "test_data") -> None:
        """Initialize test DAO with storage path identifier."""
        self.storage_path = storage_path

    def get_all_tasks(self) -> list[Task]:
        """Retrieve all tasks from test data - simulates loading from storage."""
        task_list = [
            Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)),
            Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2)),
            Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1)),
            Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)),
            Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)),
            Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))
        ]

        # Sample recurring task
        r_task = RecurringTask("Go to the gym", datetime.datetime.now(), datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
        r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)
        task_list.append(r_task)

        print(f"Loaded {len(task_list)} test tasks from {self.storage_path}")
        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        """Save all tasks - test implementation with simulated saving."""
        print(f"Simulated saving {len(tasks)} tasks to {self.storage_path}")
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task.title} - {'Completed' if task.completed else 'Not Completed'}")
