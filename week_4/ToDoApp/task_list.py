
"""
TaskList Module - Task collection management for modularized To-Do application.

Author: [VICTOR USMAN]
"""

import datetime
from task import Task

class TaskList:
    """Task collection manager for a specific owner."""

    def __init__(self, owner: str) -> None:
        """Initialize TaskList with owner name."""
        self.owner = owner.title()
        self.tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Add task to the list."""
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, ix: int) -> None:
        """Remove task by index with error handling."""
        try:
            my_task = self.tasks[ix]
            del self.tasks[ix]
            print(f"Task '{my_task}' removed.")
        except IndexError:
            print("Please enter a valid number.")

    def view_tasks(self) -> None:
        """Display all tasks with numbering."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Current tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
    