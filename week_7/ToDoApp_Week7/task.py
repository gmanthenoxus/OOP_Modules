"""
Enhanced Task Module


This module defines an enhanced Task class for the To-Do application.
It demonstrates advanced OOP concepts and features:
- Comprehensive method documentation
- Enhanced string representation
- Multiple property modification methods
- Professional code organization and documentation
- Type hints for all methods and parameters

This is the version showcasing:
- More detailed task information
- Enhanced user experience
- Professional documentation standards
- Comprehensive feature set

Author: [GLORY TITILOPE OLANREWAJU]
"""


# IMPORTS


import datetime  # Python standard library for date/time operations


# ENHANCED TASK CLASS DEFINITION


class Task:
    """
    Enhanced Task class representing a detailed task.

    This enhanced version demonstrates:
    - Comprehensive string representation
    - Multiple property modification methods
    - Professional documentation and type hints
    - Enhanced user experience features

    Attributes:
        title (str): The task title/summary
        date_created (datetime.datetime): When the task was created (auto-generated)
        date_due (datetime.datetime): When the task is due
        completed (bool): Whether the task has been completed
    """

    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        """
        Initialize a new enhanced Task instance.

        Args:
            title (str): The task title/summary
            date_due (datetime.datetime): When the task is due

        Returns:
            None: Constructors don't return values

        Example:
            >>> due_date = datetime.datetime(2024, 12, 25)
            >>> task = Task("Buy gifts", due_date)
        """
        self.title = title  # Store the task title
        self.date_created = datetime.datetime.now()  # Auto-generate creation timestamp
        self.date_due = date_due  # Store the due date
        self.completed = False  # Initialize as not completed

    def __str__(self) -> str:
        """
        Return comprehensive string representation of the enhanced Task.

        This enhanced version includes all task information in a readable format.

        Returns:
            str: Formatted string containing all task details

        Example:
            >>> print(task)
            Buy gifts [Not Completed] Created: 2024-01-15 Due: 2024-12-25
        """
        # Use conditional expression for completion status
        status = "[Completed]" if self.completed else "[Not Completed]"
        return f"{self.title} {status} Created: {self.date_created} Due: {self.date_due}"

    def mark_as_completed(self) -> None:
        """
        Mark the task as completed and provide user feedback.

        Returns:
            None: Method modifies instance state but doesn't return a value

        Example:
            >>> task.mark_as_completed()
            Task 'Buy gifts' is completed.
        """
        self.completed = True  # Set completion flag
        print(f"Task '{self.title}' is completed.")  # Provide user feedback

    def change_title(self, new_title: str) -> None:
        """
        Change the task title and provide user feedback.

        Args:
            new_title (str): The new title for the task

        Returns:
            None: Method modifies instance state but doesn't return a value

        Example:
            >>> task.change_title("Buy holiday gifts")
            Task title changed to 'Buy holiday gifts'
        """
        self.title = new_title  # Update the title
        print(f"Task title changed to '{self.title}'")  # Confirm the change

    def change_date(self, due_date: datetime.datetime) -> None:
        """
        Change the task due date and provide user feedback.

        Args:
            due_date (datetime.datetime): The new due date for the task

        Returns:
            None: Method modifies instance state but doesn't return a value

        Example:
            >>> new_date = datetime.datetime(2024, 12, 31)
            >>> task.change_date(new_date)
            Task due date changed to '2024-12-31 00:00:00'
        """
        self.date_due = due_date  # Update the due date
        print(f"Task due date changed to '{self.date_due}'")  # Confirm the change

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