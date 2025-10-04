"""
Enhanced Task Module - Portfolio Implementation

Demonstrates comprehensive OOP concepts integration:
- Abstract base classes with @abstractmethod decorator (Week 8)
- Inheritance and polymorphism (Week 5)
- Advanced task types (regular, recurring, priority)
- Professional class design and validation
- Type hints and comprehensive documentation

Author: [IKENNA FRAKLIN EZEMA]
"""

import datetime
from typing import List, Optional, Dict, ClassVar
from abc import ABC, abstractmethod


class AbstractTask(ABC):
    """Abstract base class for all task types - demonstrates Week 8 abstract classes."""

    def __init__(self, title: str, date_due: datetime.datetime, description: str = "") -> None:
        """Initialize abstract task with common attributes."""
        self.title = title
        self.date_due = date_due
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.description = description

    @abstractmethod
    def mark_as_completed(self) -> None:
        """
        Abstract method to mark task as completed.

        Must be implemented by all subclasses to handle completion logic.
        Different task types may have different completion behaviors.
        """
        pass

    @abstractmethod
    def get_task_type(self) -> str:
        """
        Abstract method to get the task type identifier.

        Returns:
            str: String identifier for the task type
        """
        pass

    def change_title(self, new_title: str) -> None:
        """Change the task title (common implementation)."""
        if not new_title.strip():
            raise ValueError("Task title cannot be empty")
        self.title = new_title.strip()
        print(f"Task title changed to '{self.title}'")

    def change_date(self, new_date: datetime.datetime) -> None:
        """Change the due date (common implementation)."""
        if new_date < datetime.datetime.now():
            print("Warning: Setting due date in the past")
        self.date_due = new_date
        print(f"Task due date changed to '{self.date_due}'")

    def change_description(self, new_description: str) -> None:
        """Change the task description (common implementation)."""
        self.description = new_description
        print(f"Task description changed to '{self.description}'")

    def is_overdue(self) -> bool:
        """Check if task is overdue (common implementation)."""
        return datetime.datetime.now() > self.date_due and not self.completed

    def days_until_due(self) -> int:
        """Calculate days until due date (common implementation)."""
        delta = self.date_due - datetime.datetime.now()
        return delta.days

    def __str__(self) -> str:
        """String representation (common implementation)."""
        status = "Completed" if self.completed else "Not Completed"
        desc_part = f" Description: {self.description}" if self.description else ""
        return f"{self.title} [{status}] Created: {self.date_created} Due: {self.date_due}{desc_part}"


# ENHANCED TASK CLASS DEFINITION


class Task(AbstractTask):
    """
    Enhanced Task class representing a basic task with description.

    This class provides concrete implementation of the abstract task interface
    for regular, non-recurring tasks with comprehensive functionality.

    Inherits all attributes from AbstractTask and implements required abstract methods.
    """

    def __init__(self, title: str, date_due: datetime.datetime, description: str = "") -> None:
        """
        Initialize a new enhanced Task instance with description.

        Args:
            title (str): The task title/summary
            date_due (datetime.datetime): When the task is due
            description (str): Optional detailed description of the task

        Example:
            >>> due_date = datetime.datetime(2024, 12, 25)
            >>> task = Task("Buy gifts", due_date, "Purchase Christmas presents for family")
        """
        super().__init__(title, date_due, description)

    def mark_as_completed(self) -> None:
        """
        Mark the regular task as completed.

        Implementation of abstract method for regular tasks.
        Sets completed flag to True and provides user feedback.
        """
        self.completed = True
        print(f"Task '{self.title}' is completed.")

    def get_task_type(self) -> str:
        """
        Get task type identifier.

        Returns:
            str: "Task" identifier for regular tasks
        """
        return "Task"


class RecurringTask(AbstractTask):
    """
    Represents a recurring task in the to-do list.

    This class demonstrates inheritance and polymorphism by extending the abstract Task class
    with recurring functionality and overriding the mark_as_completed method.

    Attributes:
        interval (datetime.timedelta): Time interval between task repetitions
        completed_dates (List[datetime.datetime]): List of dates when task was completed
    """

    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta, description: str = "") -> None:
        """
        Creates a new recurring task.

        Args:
            title (str): Title of the task
            date_due (datetime.datetime): Due date of the task
            interval (datetime.timedelta): Interval between each repetition
            description (str): Optional description of the task
        """
        super().__init__(title, date_due, description)
        self.interval = interval
        self.completed_dates: List[datetime.datetime] = []  # List of completion dates

    def _compute_next_due_date(self) -> datetime.datetime:
        """
        Computes the next due date of the task.

        Returns:
            datetime.datetime: The next due date of the task
        """
        return self.date_due + self.interval

    def mark_as_completed(self) -> None:
        """
        Override the abstract mark_as_completed method for recurring tasks.

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

    def get_task_type(self) -> str:
        """
        Get task type identifier.

        Returns:
            str: "RecurringTask" identifier for recurring tasks
        """
        return "RecurringTask"

    def __str__(self) -> str:
        """
        String representation of the recurring task.

        Returns:
            str: Formatted string showing recurring task details
        """
        completed_count = len(self.completed_dates)
        status = "Completed" if self.completed else "Not Completed"
        desc_part = f" Description: {self.description}" if self.description else ""
        return (f"{self.title} - Recurring (created: {self.date_created}, "
                f"due: {self.date_due}, completed {completed_count} times, "
                f"interval: {self.interval}){desc_part}")


# PRIORITY TASK CLASS DEFINITION


class PriorityTask(AbstractTask):
    """
    Represents a task with priority levels.

    This class demonstrates Portfolio Exercise 5 requirements:
    - Priority level stored as integer (1-3) with validation
    - Mapping from integer values to string representations
    - Enhanced string representation including priority
    - Comprehensive type annotations

    Attributes:
        priority_level (int): Priority level (1=low, 2=medium, 3=high)
        PRIORITY_MAPPING (ClassVar[Dict[int, str]]): Maps priority integers to strings
    """

    # Class variable for priority mapping (shared across all instances)
    PRIORITY_MAPPING: ClassVar[Dict[int, str]] = {
        1: "low",
        2: "medium",
        3: "high"
    }

    def __init__(self, title: str, date_due: datetime.datetime, priority_level: int, description: str = "") -> None:
        """
        Initialize a new PriorityTask with validated priority level.

        Args:
            title (str): The task title
            date_due (datetime.datetime): When the task is due
            priority_level (int): Priority level (1=low, 2=medium, 3=high)
            description (str): Optional detailed description

        Raises:
            ValueError: If priority_level is not 1, 2, or 3

        Example:
            >>> due_date = datetime.datetime(2024, 12, 25)
            >>> task = PriorityTask("Important meeting", due_date, 3, "Board meeting preparation")
        """
        super().__init__(title, date_due, description)
        self._set_priority_level(priority_level)  # Use private method for validation

    def _set_priority_level(self, priority_level: int) -> None:
        """
        Private method to set and validate priority level.

        This ensures that no invalid priority values can be stored,
        demonstrating proper encapsulation and validation.

        Args:
            priority_level (int): Priority level to validate and set

        Raises:
            ValueError: If priority_level is not 1, 2, or 3
        """
        if priority_level not in self.PRIORITY_MAPPING:
            valid_levels = list(self.PRIORITY_MAPPING.keys())
            raise ValueError(f"Priority level must be one of {valid_levels}, got {priority_level}")

        self._priority_level = priority_level

    @property
    def priority_level(self) -> int:
        """
        Get the priority level as an integer.

        Returns:
            int: Priority level (1, 2, or 3)
        """
        return self._priority_level

    @priority_level.setter
    def priority_level(self, value: int) -> None:
        """
        Set the priority level with validation.

        Args:
            value (int): New priority level (1, 2, or 3)

        Raises:
            ValueError: If value is not 1, 2, or 3
        """
        self._set_priority_level(value)
        print(f"Priority level changed to {value} ({self.get_priority_string()})")

    def get_priority_string(self) -> str:
        """
        Get the priority level as a human-readable string.

        Uses the PRIORITY_MAPPING to convert integer to string representation.

        Returns:
            str: Priority level as string ("low", "medium", or "high")

        Example:
            >>> task = PriorityTask("Test", datetime.datetime.now(), 3)
            >>> task.get_priority_string()
            'high'
        """
        return self.PRIORITY_MAPPING[self._priority_level]

    def mark_as_completed(self) -> None:
        """
        Mark the priority task as completed.

        Implementation of abstract method for priority tasks.
        Includes priority information in the completion message.
        """
        self.completed = True
        priority_str = self.get_priority_string()
        print(f"{priority_str.capitalize()} priority task '{self.title}' is completed.")

    def get_task_type(self) -> str:
        """
        Get task type identifier.

        Returns:
            str: "PriorityTask" identifier for priority tasks
        """
        return "PriorityTask"

    def __str__(self) -> str:
        """
        Enhanced string representation including priority information.

        This demonstrates the requirement for suitable string representation
        that uses the mapping attribute and returns task details with priority.

        Returns:
            str: Formatted string with all task details including priority

        Example:
            >>> print(task)
            Important meeting [Not Completed] Priority: high Created: 2024-1-15 Due: 2024-12-25 Description: Board meeting
        """
        status = "Completed" if self.completed else "Not Completed"
        priority_str = self.get_priority_string()
        desc_part = f" Description: {self.description}" if self.description else ""

        return (f"{self.title} [{status}] Priority: {priority_str} "
                f"Created: {self.date_created} Due: {self.date_due}{desc_part}")

    @classmethod
    def get_valid_priority_levels(cls) -> List[int]:
        """
        Class method to get all valid priority levels.

        Returns:
            List[int]: List of valid priority level integers
        """
        return list(cls.PRIORITY_MAPPING.keys())

    @classmethod
    def get_priority_descriptions(cls) -> Dict[int, str]:
        """
        Class method to get the complete priority mapping.

        Returns:
            Dict[int, str]: Complete mapping of priority levels to descriptions
        """
        return cls.PRIORITY_MAPPING.copy()