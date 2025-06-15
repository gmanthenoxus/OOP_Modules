"""
Week 4 Lab - Object-Oriented Programming and Classes
====================================================

This lab demonstrates fundamental Object-Oriented Programming concepts including:
- Class definition and instantiation
- Constructor methods (__init__)
- Instance variables and methods
- Method parameters and type hints
- Python libraries and imports
- Interactive menu systems with classes
- DateTime manipulation and formatting
- Error handling within class methods
- String representation methods (__str__)

Key OOP Concepts Covered:
- Encapsulation: Data and methods bundled together in classes
- Abstraction: Complex functionality hidden behind simple interfaces
- Code Organization: Related functionality grouped in classes
- Reusability: Classes can be instantiated multiple times

Author: [Student Name]
Date: [Date]
"""

# =============================================================================
# PYTHON LIBRARIES AND IMPORTS
# =============================================================================

# Importing datetime module (Python Standard Library)
# The datetime module provides classes for working with dates and times
import datetime

# =============================================================================
# CLASS DEFINITIONS - OBJECT-ORIENTED PROGRAMMING
# =============================================================================

class TaskList:
    """
    A class to represent a task list with an owner and collection of tasks.

    This class demonstrates fundamental OOP concepts:
    - Encapsulation: Data (owner, tasks) and methods bundled together
    - Constructor: __init__ method initializes new instances
    - Instance methods: Functions that operate on instance data
    - Type hints: Specify expected parameter types for better code documentation

    Attributes:
        owner (str): The name of the task list owner (title case)
        tasks (list): A list of Task objects
    """

    def __init__(self, owner: str) -> None:
        """
        Constructor method - initializes a new TaskList instance.

        This method is automatically called when creating a new TaskList object.
        It sets up the initial state of the object.

        Args:
            owner (str): The name of the person who owns this task list

        Returns:
            None: Constructors don't return values
        """
        self.owner = owner.title()  # Convert to title case (e.g., "john" -> "John")
        self.tasks = []  # Initialize empty list to store Task objects

    def add_task(self, task: 'Task') -> None:
        """
        Adds a task to the task list.

        Args:
            task (Task): A Task object to add to the list

        Returns:
            None: Method modifies the instance but doesn't return a value
        """
        self.tasks.append(task)  # Add task to the tasks list
        print(f"Task '{task}' added.")  # Provide user feedback

    def remove_task(self, ix: int) -> None:
        """
        Removes a task from the list by index with error handling.

        Args:
            ix (int): The index of the task to remove (0-based)

        Returns:
            None: Method modifies the instance but doesn't return a value
        """
        try:
            my_task = self.tasks[ix]  # Get task at specified index
            del self.tasks[ix]  # Remove task from list
            print(f"Task '{my_task}' removed.")  # Confirm removal
        except IndexError:  # Handle case where index doesn't exist
            print("Please enter a valid number.")

    def view_tasks(self) -> None:
        """
        Displays all tasks in the list with numbering.

        Returns:
            None: Method prints to console but doesn't return a value
        """
        if not self.tasks:  # Check if list is empty
            print("No tasks in the list.")
        else:
            print("Current tasks:")
            # Use enumerate to get both index and task, starting from 1
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")  # Print task number and task details

    def list_options(self) -> None:
        """
        Main interactive menu system for the task list application.

        This method demonstrates:
        - While loops for continuous program execution
        - User input handling and validation
        - Menu-driven program structure
        - Integration of multiple class methods
        - DateTime parsing and object creation

        Returns:
            None: Method runs until user chooses to quit
        """
        while True:  # Infinite loop until user chooses to quit
            # Display menu options
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark task as completed")
            print("5. Edit task")
            print("6. Quit")

            choice = input("Enter your choice: ")  # Get user's menu selection

            # Process user choice using if-elif-else structure
            if choice == "1":  # Add a new task
                title = input("Enter the task you want to add:  ")
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                # Convert string date to datetime object using strptime
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)  # Create new Task instance
                self.add_task(task)  # Add task to list using class method

            elif choice == "2":  # View all tasks
                self.view_tasks()  # Call view_tasks method

            elif choice == "3":  # Remove a task
                self.view_tasks()  # Show tasks first so user can see numbers
                if not self.tasks:  # If no tasks, continue to next iteration
                    continue
                else:
                    ix = int(input("Enter the task number to remove: "))
                    self.remove_task(ix - 1)  # Convert to 0-based index

            elif choice == "4":  # Mark task as completed
                self.view_tasks()  # Show tasks first
                if not self.tasks:  # If no tasks, continue
                    continue
                else:
                    completed = int(input("Enter the task number to mark as completed: "))
                    # Call mark_as_completed method on specific task
                    self.tasks[completed - 1].mark_as_completed()

            elif choice == "5":  # Edit a task
                self.view_tasks()  # Show tasks first
                if not self.tasks:  # If no tasks, continue
                    continue
                else:
                    title_num = int(input("Enter the task to Edit: "))
                    # Validate task number is within range
                    if 1 <= title_num <= len(self.tasks):
                        edit = input("Do you want to edit the title,due date or both? (title/date/both): ").lower()

                        if edit == "title" or edit == "t":  # Edit title only
                            new_title = input("Enter the new title: ")
                            self.tasks[title_num - 1].change_title(new_title)

                        elif edit == "date" or edit == "d":  # Edit date only
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            # Direct assignment to date_due attribute
                            self.tasks[title_num - 1].date_due = date_object

                        elif edit == "both" or edit == "b":  # Edit both title and date
                            new_title = input("Enter the new title: ")
                            self.tasks[title_num - 1].change_title(new_title)
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            self.tasks[title_num - 1].date_due = date_object

                        else:  # Invalid edit choice
                            print("Invalid choice. Please try again.")
                            continue
                    else:  # Invalid task number
                        print("Invalid task number.")

            elif choice == "6":  # Quit program
                print("Exiting program. Goodbye!")
                break  # Exit the while loop

            else:  # Invalid menu choice
                print("Invalid choice. Please try again.")

class Task:
    """
    A class to represent an individual task with title, dates, and completion status.

    This class demonstrates:
    - Constructor with multiple parameters
    - Instance attributes for storing task data
    - Special methods (__str__) for string representation
    - Instance methods for modifying task properties
    - Boolean attributes for tracking state
    - DateTime handling for task scheduling

    Attributes:
        title (str): The task description/title
        date_created (datetime): When the task was created (auto-generated)
        date_due (datetime): When the task is due
        completed (bool): Whether the task has been completed
    """

    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        """
        Constructor method - initializes a new Task instance.

        Note: The original constructor signature had extra parameters that weren't used.
        This version uses only the necessary parameters.

        Args:
            title (str): The task description/title
            date_due (datetime.datetime): When the task is due

        Returns:
            None: Constructors don't return values
        """
        self.title = title  # Store task title
        self.date_created = datetime.datetime.now()  # Auto-generate creation time
        self.date_due = date_due  # Store due date
        self.completed = False  # Initialize as not completed

    def __str__(self) -> str:
        """
        Special method that defines string representation of Task objects.

        This method is automatically called when:
        - Using print() on a Task object
        - Converting Task to string with str()
        - Using f-strings with Task objects

        Returns:
            str: A formatted string showing task details
        """
        # Use conditional expression to show completion status
        status = "[Completed]" if self.completed else "[Not Completed]"
        return f"{self.title} {status} Created: {self.date_created} Due: {self.date_due}"

    def mark_as_completed(self) -> None:
        """
        Marks the task as completed and provides user feedback.

        This method demonstrates:
        - Modifying instance attributes
        - Providing user feedback
        - Simple state management

        Returns:
            None: Method modifies instance but doesn't return a value
        """
        self.completed = True  # Set completion status to True
        print(f"Task '{self.title}' is completed.")  # Provide confirmation

    def change_title(self, new_title: str) -> None:
        """
        Changes the task title and provides user feedback.

        Args:
            new_title (str): The new title for the task

        Returns:
            None: Method modifies instance but doesn't return a value
        """
        self.title = new_title  # Update the title
        print(f"Task title changed to '{self.title}'")  # Confirm change

# =============================================================================
# MAIN PROGRAM EXECUTION
# =============================================================================

# Get user input for task list owner
input_owner = input("Enter the name of the owner: ")

# Create a new TaskList instance (object instantiation)
task_list = TaskList(input_owner)

# Welcome message using the owner attribute
print(f"Welcome {task_list.owner}")

# Start the interactive menu system
task_list.list_options()
