
"""
TaskList Module - Task Collection Management
===========================================

This module defines the TaskList class for managing collections of tasks.
It demonstrates:
- Module imports and dependencies
- Class composition (TaskList contains Task objects)
- Type hints with generic types (list[Task])
- Error handling within class methods
- Collection management operations (add, remove, view)
- Enumeration and iteration over collections

This module works with:
- task.py: Imports Task class for type hints and object creation
- main.py: Uses TaskList class for application logic

Author: [Student Name]
Date: [Date]
"""

# =============================================================================
# IMPORTS
# =============================================================================

import datetime  # For date/time operations (if needed for future enhancements)
from task import Task  # Import Task class from task module

# =============================================================================
# TASKLIST CLASS DEFINITION
# =============================================================================

class TaskList:
    """
    Manages a collection of tasks for a specific owner.

    This class demonstrates:
    - Composition: TaskList contains multiple Task objects
    - Collection management: Adding, removing, and viewing tasks
    - Type hints with generics: list[Task] specifies list contents
    - Error handling: Graceful handling of invalid operations
    - User feedback: Informative messages for all operations

    Attributes:
        owner (str): The name of the task list owner (title case)
        tasks (list[Task]): A list containing Task objects
    """

    def __init__(self, owner: str) -> None:
        """
        Initialize a new TaskList instance.

        Args:
            owner (str): The name of the person who owns this task list

        Returns:
            None: Constructors don't return values

        Example:
            >>> task_list = TaskList("john doe")
            >>> print(task_list.owner)  # Output: "John Doe"
        """
        self.owner = owner.title()  # Convert to title case for consistency
        self.tasks: list[Task] = []  # Initialize empty list with type hint

    def add_task(self, task: Task) -> None:
        """
        Add a task to the task list.

        Args:
            task (Task): A Task object to add to the collection

        Returns:
            None: Method modifies instance but doesn't return a value

        Example:
            >>> task = Task("Buy groceries", datetime.datetime.now())
            >>> task_list.add_task(task)
            Task 'Buy groceries [Not Completed] ...' added.
        """
        self.tasks.append(task)  # Add task to the collection
        print(f"Task '{task}' added.")  # Provide user feedback

    def remove_task(self, ix: int) -> None:
        """
        Remove a task from the list by index with error handling.

        This method demonstrates proper error handling for list operations,
        preventing crashes when invalid indices are provided.

        Args:
            ix (int): The index of the task to remove (0-based)

        Returns:
            None: Method modifies instance but doesn't return a value

        Example:
            >>> task_list.remove_task(0)  # Remove first task
            Task 'Buy groceries [Not Completed] ...' removed.
        """
        try:
            my_task = self.tasks[ix]  # Get task at specified index
            del self.tasks[ix]  # Remove task from list
            print(f"Task '{my_task}' removed.")  # Confirm removal
        except IndexError:  # Handle invalid index gracefully
            print("Please enter a valid number.")

    def view_tasks(self) -> None:
        """
        Display all tasks in the list with numbering.

        This method demonstrates:
        - Conditional logic for empty collections
        - Enumeration for user-friendly numbering
        - Iteration over custom objects

        Returns:
            None: Method prints to console but doesn't return a value

        Example:
            >>> task_list.view_tasks()
            Current tasks:
            1. Buy groceries [Not Completed] Created: ... Due: ...
            2. Do laundry [Completed] Created: ... Due: ...
        """
        if not self.tasks:  # Check if collection is empty
            print("No tasks in the list.")
        else:
            print("Current tasks:")
            # Use enumerate to provide user-friendly numbering (1-based)
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")  # Print number and task details
    