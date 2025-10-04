"""
Enhanced Task Module - Week 6 Property Decorators and Persistence

Demonstrates @property decorators for computed attributes:
- Computed properties like uncompleted_tasks
- Data persistence preparation for DAO pattern
- Enhanced task management with property access

Author: [MOSES GANA]
"""

import datetime


class Task:
    """Enhanced Task class with property decorators for computed attributes."""

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
    """
    Represents a recurring task in a to-do list.

    This class demonstrates inheritance and polymorphism by extending the base Task class
    with recurring functionality and overriding the mark_as_completed method.

    Attributes:
        interval (datetime.timedelta): Time interval between task repetitions
        completed_dates (list[datetime.datetime]): List of dates when task was completed
    """

    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        """
        Creates a new recurring task.

        Args:
            title (str): Title of the task
            date_due (datetime.datetime): Due date of the task
            interval (datetime.timedelta): Interval between each repetition
        """
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: list[datetime.datetime] = []  # List of completion dates

    def _compute_next_due_date(self) -> datetime.datetime:
        """
        Computes the next due date of the task.

        Returns:
            datetime.datetime: The next due date of the task
        """
        return self.date_due + self.interval

    def mark_as_completed(self) -> None:
        """
        Override the parent's mark_as_completed method to implement polymorphism.

        For recurring tasks, marking as completed:
        1. Adds current date to completed_dates list
        2. Updates the due date to the next occurrence
        3. Keeps the task as not completed so it appears again

        This demonstrates polymorphism - same method name, different behavior.
        """
        # Add current date to completed dates
        self.completed_dates.append(datetime.datetime.now())

        # Update due date to next occurrence
        self.date_due = self._compute_next_due_date()

        # Provide user feedback
        print(f"Recurring task '{self.title}' completed. Next due date: {self.date_due}")

        # Note: We don't set self.completed = True because it's a recurring task

    def __str__(self) -> str:
        """
        String representation of the recurring task.

        Returns:
            str: Formatted string showing recurring task details
        """
        completed_count = len(self.completed_dates)
        return f"{self.title} - Recurring (created: {self.date_created}, due: {self.date_due}, completed {completed_count} times, interval: {self.interval})"