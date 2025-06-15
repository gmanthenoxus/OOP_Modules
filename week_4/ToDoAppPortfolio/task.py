"""
Enhanced Task Module - Portfolio Project
========================================

This module defines an enhanced Task class for the portfolio To-Do application.
It demonstrates advanced OOP concepts and features:
- Extended class attributes (description field)
- Comprehensive method documentation
- Enhanced string representation
- Multiple property modification methods
- Professional code organization and documentation
- Type hints for all methods and parameters

This is the portfolio version showcasing:
- More detailed task information
- Enhanced user experience
- Professional documentation standards
- Comprehensive feature set

Author: [Student Name]
Date: [Date]
"""

# =============================================================================
# IMPORTS
# =============================================================================

import datetime  # Python standard library for date/time operations

# =============================================================================
# ENHANCED TASK CLASS DEFINITION
# =============================================================================

class Task:
    """
    Enhanced Task class representing a detailed task with description.

    This enhanced version demonstrates:
    - Extended data model with description field
    - Comprehensive string representation
    - Multiple property modification methods
    - Professional documentation and type hints
    - Enhanced user experience features

    Attributes:
        title (str): The task title/summary
        date_created (datetime.datetime): When the task was created (auto-generated)
        date_due (datetime.datetime): When the task is due
        completed (bool): Whether the task has been completed
        description (str): Detailed description of the task
    """

    def __init__(self, title: str, date_due: datetime.datetime, description: str) -> None:
        """
        Initialize a new enhanced Task instance with description.

        Args:
            title (str): The task title/summary
            date_due (datetime.datetime): When the task is due
            description (str): Detailed description of the task

        Returns:
            None: Constructors don't return values

        Example:
            >>> due_date = datetime.datetime(2024, 12, 25)
            >>> task = Task("Buy gifts", due_date, "Purchase Christmas presents for family")
        """
        self.title = title  # Store the task title
        self.date_created = datetime.datetime.now()  # Auto-generate creation timestamp
        self.date_due = date_due  # Store the due date
        self.completed = False  # Initialize as not completed
        self.description = description  # Store detailed description

    def __str__(self) -> str:
        """
        Return comprehensive string representation of the enhanced Task.

        This enhanced version includes all task information in a readable format.

        Returns:
            str: Formatted string containing all task details including description

        Example:
            >>> print(task)
            Buy gifts [Not Completed] Created: 2024-01-15 Due: 2024-12-25 Description: Purchase Christmas presents for family
        """
        # Use conditional expression for completion status
        status = "[Completed]" if self.completed else "[Not Completed]"
        return f"{self.title} {status} Created: {self.date_created} Due: {self.date_due} Description: {self.description}"

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

    def change_description(self, new_description: str) -> None:
        """
        Change the task description and provide user feedback.

        This method is unique to the enhanced portfolio version,
        demonstrating extended functionality.

        Args:
            new_description (str): The new description for the task

        Returns:
            None: Method modifies instance state but doesn't return a value

        Example:
            >>> task.change_description("Buy presents and wrap them nicely")
            Task description changed to 'Buy presents and wrap them nicely'
        """
        self.description = new_description  # Update the description
        print(f"Task description changed to '{self.description}'")  # Confirm the change