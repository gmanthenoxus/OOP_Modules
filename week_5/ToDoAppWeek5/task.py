"""
Enhanced Task Module - Week 5 OOP Concepts

Demonstrates inheritance, polymorphism, and method overriding:
- Base Task class with standard functionality
- RecurringTask class inheriting from Task
- Polymorphic mark_as_completed method
- Enhanced string representation

Author: [VICTOR NNAMDI EKWEMALOR]
"""

import datetime


class Task:
    """Base task class with standard functionality."""

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

class RecurringTask(Task):
    """Recurring task demonstrating inheritance and polymorphism."""

    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        """Initialize recurring task with interval."""
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: list[datetime.datetime] = []

    def _compute_next_due_date(self) -> datetime.datetime:
        """Compute next due date based on interval."""
        return self.date_due + self.interval

    def mark_as_completed(self) -> None:
        """Override parent method - demonstrates polymorphism."""
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()
        print(f"Recurring task '{self.title}' completed. Next due date: {self.date_due}")

    def __str__(self) -> str:
        """String representation showing recurring task details."""
        completed_count = len(self.completed_dates)
        return f"{self.title} - Recurring (created: {self.date_created}, due: {self.date_due}, completed {completed_count} times, interval: {self.interval})"