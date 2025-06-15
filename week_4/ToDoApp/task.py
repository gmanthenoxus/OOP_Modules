"""
Task Module - Object-Oriented Task Management
=============================================

This module defines the Task class for the modularized To-Do application.
It demonstrates:
- Module-level documentation
- Class definition with type hints
- Special methods (__str__)
- Instance methods with proper documentation
- DateTime handling and manipulation
- Code organization and separation of concerns

This is part of a modularized application structure where:
- task.py: Contains Task class definition
- task_list.py: Contains TaskList class definition
- main.py: Contains application logic and user interface

Author: [Student Name]
Date: [Date]
"""

# =============================================================================
# IMPORTS - PYTHON STANDARD LIBRARY
# =============================================================================

# Importing datetime module for date and time operations
import datetime

# =============================================================================
# TASK CLASS DEFINITION
# =============================================================================

class Task:
    """
    Represents an individual task with title, dates, and completion status.

    This class encapsulates all data and behavior related to a single task,
    demonstrating key OOP principles:
    - Encapsulation: Data and methods bundled together
    - Abstraction: Complex date handling hidden behind simple interface
    - Data integrity: Controlled access to task properties

    Attributes:
        title (str): The task description/title
        date_created (datetime.datetime): When the task was created (auto-generated)
        date_due (datetime.datetime): When the task is due
        completed (bool): Whether the task has been completed
    """

    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        """
        Initialize a new Task instance.

        The constructor sets up the initial state of a task with automatic
        timestamp generation for creation date.

        Args:
            title (str): The task description/title
            date_due (datetime.datetime): When the task is due

        Returns:
            None: Constructors don't return values

        Example:
            >>> due_date = datetime.datetime(2024, 12, 25)
            >>> task = Task("Buy Christmas gifts", due_date)
        """
        self.title = title  # Store the task title
        self.date_created = datetime.datetime.now()  # Auto-generate creation timestamp
        self.date_due = date_due  # Store the due date
        self.completed = False  # Initialize as not completed

    def __str__(self) -> str:
        """
        Return string representation of the Task object.

        This special method (dunder method) is automatically called when:
        - Using print() with a Task object
        - Converting Task to string with str()
        - Using Task objects in f-strings

        Returns:
            str: Formatted string containing task details

        Example:
            >>> print(task)
            Buy Christmas gifts [Not Completed] Created: 2024-01-15 Due: 2024-12-25
        """
        # Use conditional expression for completion status
        status = "[Completed]" if self.completed else "[Not Completed]"
        return f"{self.title} {status} Created: {self.date_created} Due: {self.date_due}"

    def mark_as_completed(self) -> None:
        """
        Mark the task as completed and provide user feedback.

        This method changes the task's completion status and provides
        immediate feedback to the user.

        Returns:
            None: Method modifies instance state but doesn't return a value

        Example:
            >>> task.mark_as_completed()
            Task 'Buy Christmas gifts' is completed.
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