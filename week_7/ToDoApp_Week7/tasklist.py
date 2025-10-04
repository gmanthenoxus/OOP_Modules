"""
Enhanced TaskList Module - Week 7 SOLID Principles

Demonstrates SOLID principles and enhanced functionality:
- Single Responsibility Principle (task list management)
- DRY principle with check_task_index method
- Enhanced error handling and validation
- @property decorators for computed attributes

Author: [GLORY TITILOPE OLANREWAJU]
"""

import datetime
from task import Task, RecurringTask


class TaskList:
    """
    Enhanced TaskList class with advanced task management features.

    This enhanced version demonstrates:
    - Advanced filtering capabilities (overdue tasks)
    - Date/time comparisons and logic
    - Professional code organization
    - Comprehensive documentation

    Attributes:
        owner (str): The name of the task list owner (title case)
        tasks (list[Task]): A list containing enhanced Task objects
    """

    def __init__(self, owner: str) -> None:
        """
        Initialize a new enhanced TaskList instance.

        Args:
            owner (str): The name of the person who owns this task list

        Returns:
            None: Constructors don't return values

        Example:
            >>> task_list = TaskList("jane smith")
            >>> print(task_list.owner)  # Output: "Jane Smith"
        """
        self.owner = owner.title()  # Convert to title case for consistency
        self.tasks: list[Task] = []  # Initialize empty list with type hint

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

    @property
    def uncompleted_tasks(self) -> list[Task]:
        """
        Property to get all uncompleted tasks using list comprehension.

        This property demonstrates:
        - Use of @property decorator for attribute-like access
        - List comprehension for elegant filtering
        - Encapsulation of filtering logic

        Returns:
            list[Task]: A list of all tasks that are not completed

        Example:
            >>> uncompleted = task_list.uncompleted_tasks
            >>> print(len(uncompleted))  # Number of uncompleted tasks
        """
        return [task for task in self.tasks if not task.completed]

    def view_tasks(self) -> None:
        """
        Display only uncompleted tasks with proper indexing.

        This method now uses the uncompleted_tasks property to show only
        tasks that are still to be done, demonstrating the use of properties
        for computed attributes.

        Returns:
            None: Method prints to console but doesn't return a value

        Example:
            >>> task_list.view_tasks()
            The following tasks are still to be done:
            1. Buy groceries [Not Completed] Created: ... Due: ... Description: Weekly shopping
        """
        if not self.uncompleted_tasks:  # Check if there are uncompleted tasks
            print("No uncompleted tasks in the list.")
        else:
            print("The following tasks are still to be done:")
            # Use the index() method to get the correct index for each uncompleted task
            for task in self.uncompleted_tasks:
                ix = self.tasks.index(task) + 1  # Get 1-based index from original list
                print(f"{ix}: {task}")  # Print index and task details

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

    def check_task_index(self, ix: int) -> bool:
        """Check if task index is valid - demonstrates DRY principle."""
        return 0 <= ix < len(self.tasks)

    def get_task(self, index: int) -> Task:
        """Get task at specified index using DRY principle validation."""
        if self.check_task_index(index):
            return self.tasks[index]
        else:
            raise IndexError("Task index out of range")

