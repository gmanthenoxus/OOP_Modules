"""
Enhanced TaskList Module - Week 5 OOP Concepts

Demonstrates encapsulation and proper access control:
- get_task method for controlled access
- Enhanced task filtering capabilities
- Professional collection management

Author: [VICTOR NNAMDI EKWEMALOR]
"""

import datetime
from task import Task, RecurringTask


class TaskList:
    """Enhanced TaskList with encapsulation and filtering capabilities."""

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

    def view_overdue_tasks(self) -> None:
        """Display only overdue tasks with numbering."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Overdue tasks:")
            overdue_count = 0

            for i, task in enumerate(self.tasks, start=1):
                if task.date_due < datetime.datetime.now():
                    print(f"{i}. {task}")
                    overdue_count += 1

            if overdue_count == 0:
                print("No overdue tasks found.")

    def get_task(self, index: int) -> Task:
        """Get task at specified index - demonstrates encapsulation."""
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        else:
            raise IndexError("Task index out of range")

