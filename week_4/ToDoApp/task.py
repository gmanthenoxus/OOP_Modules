"""
Task Module - Task class definition for modularized To-Do application.

Author: [VICTOR USMAN]
"""

import datetime

class Task:
    """Individual task with title, dates, and completion status."""

    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        """Initialize Task with title and due date."""
        self.title = title
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.completed = False

    def __str__(self) -> str:
        """Return formatted string representation of task."""
        status = "[Completed]" if self.completed else "[Not Completed]"
        return f"{self.title} {status} Created: {self.date_created} Due: {self.date_due}"

    def mark_as_completed(self) -> None:
        """Mark task as completed."""
        self.completed = True
        print(f"Task '{self.title}' is completed.")

    def change_title(self, new_title: str) -> None:
        """Change task title."""
        self.title = new_title
        print(f"Task title changed to '{self.title}'")

    def change_date(self, due_date: datetime.datetime) -> None:
        """Change task due date."""
        self.date_due = due_date
        print(f"Task due date changed to '{self.date_due}'")