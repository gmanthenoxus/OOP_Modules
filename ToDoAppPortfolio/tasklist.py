"""
Enhanced TaskList Module - Portfolio Project


This module defines an enhanced TaskList class for the portfolio To-Do application.
It demonstrates advanced features and functionality:
- Enhanced task filtering (overdue tasks)
- Improved date/time comparisons
- Professional documentation standards
- Advanced collection management
- Portfolio-quality code organization

This enhanced version showcases:
- Additional functionality (overdue task filtering)
- More sophisticated date handling
- Professional development practices
- Comprehensive error handling and user feedback

Author: [Moses Gana]
"""


# IMPORTS


import datetime  # For date/time operations and comparisons
from task import Task, RecurringTask  # Import enhanced Task classes from task module
from users import Owner  # Import Owner class from users module


# ENHANCED TASKLIST CLASS DEFINITION


class TaskList:
    """
    Enhanced TaskList class with advanced task management features.

    This enhanced version demonstrates:
    - Advanced filtering capabilities (overdue tasks)
    - Date/time comparisons and logic
    - Professional code organization
    - Comprehensive documentation
    - Portfolio-quality implementation
    - Owner-based task list management

    Attributes:
        owner (Owner): The Owner instance who owns this task list
        tasks (list[Task]): A list containing enhanced Task objects
    """

    def __init__(self, owner: Owner) -> None:
        """
        Initialize a new enhanced TaskList instance with Owner.

        Args:
            owner (Owner): The Owner instance who owns this task list

        Returns:
            None: Constructors don't return values

        Example:
            >>> owner = Owner("jane smith", "jane@example.com")
            >>> task_list = TaskList(owner)
            >>> print(task_list.owner.name)  # Output: "Jane Smith"
        """
        self.owner = owner  # Store Owner instance
        self.tasks: list[Task] = []  # Initialize empty list with type hint
        self.owner.create_task_list()  # Increment owner's task list counter

    def add_task(self, task: Task) -> None:
        """
        Add an enhanced task to the task list.

        Args:
            task (Task): An enhanced Task object to add to the collection

        Returns:
            None: Method modifies instance but doesn't return a value

        Example:
            >>> task = Task("Buy groceries", datetime.datetime.now(), "Weekly shopping")
            >>> task_list.add_task(task)
            Task 'Buy groceries [Not Completed] ...' added.
        """
        self.tasks.append(task)  # Add task to the collection
        print(f"Task '{task}' added.")  # Provide user feedback

    def remove_task(self, ix: int) -> None:
        """
        Remove a task from the list by index with error handling.

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

        Returns:
            None: Method prints to console but doesn't return a value

        Example:
            >>> task_list.view_tasks()
            Current tasks:
            1. Buy groceries [Not Completed] Created: ... Due: ... Description: Weekly shopping
        """
        if not self.tasks:  # Check if collection is empty
            print("No tasks in the list.")
        else:
            print("Current tasks:")
            # Use enumerate to provide user-friendly numbering (1-based)
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")  # Print number and task details

    def view_overdue_tasks(self) -> None:
        """
        Display only overdue tasks with numbering.

        This enhanced method demonstrates:
        - Date/time comparisons
        - Conditional filtering of collections
        - Advanced task management features
        - Real-time date calculations

        A task is considered overdue if its due date is before the current time.

        Returns:
            None: Method prints to console but doesn't return a value

        Example:
            >>> task_list.view_overdue_tasks()
            Overdue tasks:
            1. Buy groceries [Not Completed] Created: ... Due: 2024-01-10 Description: Weekly shopping
        """
        if not self.tasks:  # Check if collection is empty
            print("No tasks in the list.")
        else:
            print("Overdue tasks:")
            overdue_count = 0  # Track number of overdue tasks found

            # Iterate through all tasks to find overdue ones
            for i, task in enumerate(self.tasks, start=1):
                # Compare task due date with current time
                if task.date_due < datetime.datetime.now():
                    print(f"{i}. {task}")  # Print overdue task details
                    overdue_count += 1

            # Provide feedback if no overdue tasks found
            if overdue_count == 0:
                print("No overdue tasks found.")

    def get_task(self, index: int) -> Task:
        """
        Get a task at the specified index using encapsulation.

        This method provides controlled access to tasks instead of directly
        accessing the tasks list. This demonstrates encapsulation - hiding
        the internal implementation details from the user.

        Args:
            index (int): The index of the task to retrieve (0-based)

        Returns:
            Task: The task at the specified index

        Raises:
            IndexError: If the index is out of range

        Example:
            >>> task = task_list.get_task(0)  # Get first task
        """
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        else:
            raise IndexError("Task index out of range")
