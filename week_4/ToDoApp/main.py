"""
Main Application Module - Modularized To-Do List Manager
========================================================

This module serves as the main entry point for the modularized To-Do application.
It demonstrates:
- Module imports and organization
- Separation of concerns (UI logic separate from data classes)
- Function-based program structure
- Comprehensive error handling
- Type hints for function parameters and return values
- Interactive menu systems
- DateTime parsing and manipulation
- Testing utilities for development

Module Dependencies:
- task_list.py: Provides TaskList class
- task.py: Provides Task class
- datetime: Python standard library for date/time operations

Author: [Student Name]
Date: [Date]
"""

# =============================================================================
# IMPORTS - MODULE DEPENDENCIES
# =============================================================================

from task_list import TaskList  # Import TaskList class from task_list module
import datetime  # Python standard library for date/time operations
from task import Task  # Import Task class from task module

# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================

def propagate_task_list(task_list: TaskList) -> TaskList:
    """
    Populate a task list with sample tasks for testing purposes.

    This function demonstrates:
    - Function type hints with custom classes
    - DateTime arithmetic with timedelta
    - Task creation with various due dates
    - Function documentation with proper formatting

    Args:
        task_list (TaskList): The task list to populate with sample data

    Returns:
        TaskList: The same task list instance with added sample tasks

    Example:
        >>> task_list = TaskList("Test User")
        >>> populated_list = propagate_task_list(task_list)
        >>> len(populated_list.tasks)  # Should be 6
    """
    # Create sample tasks with various due dates (past, present, future)
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2)))
    task_list.add_task(Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))
    return task_list

# =============================================================================
# MAIN APPLICATION FUNCTION
# =============================================================================

def main() -> None:
    """
    Main application function that runs the interactive To-Do list manager.

    This function demonstrates:
    - Application initialization and setup
    - Interactive menu systems with comprehensive error handling
    - User input validation and processing
    - Integration of multiple classes and modules
    - Exception handling hierarchy (specific to general)
    - Program flow control with loops and conditionals

    Returns:
        None: Function runs until user chooses to quit
    """
    # Application initialization
    input_owner = input("Enter the name of the owner: ")
    task_list = TaskList(input_owner)  # Create TaskList instance

    # Uncomment the next line to populate with sample data for testing
    # task_list = propagate_task_list(task_list)

    print(f"Welcome {task_list.owner}")  # Welcome message

    # Main application loop with comprehensive error handling
    while True:
        try:
            # Display menu options
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark task as completed")
            print("5. Edit task")
            print("6. Quit")

            choice = input("Enter your choice: ")  # Get user selection

            if choice == "1":  # Add a new task
                title = input("Enter the task you want to add:  ")
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                # Parse string date into datetime object
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)  # Create Task instance
                task_list.add_task(task)  # Add to task list

            elif choice == "2":  # View all tasks
                task_list.view_tasks()

            elif choice == "3":  # Remove a task
                task_list.view_tasks()  # Show tasks first
                if not task_list.tasks:  # Check if list is empty
                    continue  # Skip to next iteration if no tasks
                else:
                    ix = int(input("Enter the task number to remove: "))
                    task_list.remove_task(ix - 1)  # Convert to 0-based index

            elif choice == "4":  # Mark task as completed
                task_list.view_tasks()  # Show tasks first
                if not task_list.tasks:  # Check if list is empty
                    continue
                else:
                    completed = int(input("Enter the task number to mark as completed: "))
                    # Call method on specific task object
                    task_list.tasks[completed - 1].mark_as_completed()

            elif choice == "5":  # Edit a task
                task_list.view_tasks()  # Show tasks first
                if not task_list.tasks:  # Check if list is empty
                    continue
                else:
                    title_num = int(input("Enter the task to Edit: "))
                    # Validate task number is within range
                    if 1 <= title_num <= len(task_list.tasks):
                        edit = input("Do you want to edit the title,due date or both? (title/date/both): ").lower()

                        if edit == "title" or edit == "t":  # Edit title only
                            new_title = input("Enter the new title: ")
                            task_list.tasks[title_num - 1].change_title(new_title)

                        elif edit == "date" or edit == "d":  # Edit date only
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            task_list.tasks[title_num - 1].change_date(date_object)

                        elif edit == "both" or edit == "b":  # Edit both
                            new_title = input("Enter the new title: ")
                            task_list.tasks[title_num - 1].change_title(new_title)
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            task_list.tasks[title_num - 1].change_date(date_object)

                        else:  # Invalid edit choice
                            print("Invalid choice. Please try again.")
                            continue
                    else:  # Invalid task number
                        print("Invalid task number.")

            elif choice == "6":  # Quit application
                print("Exiting program. Goodbye!")
                break  # Exit the main loop

            else:  # Invalid menu choice
                print("Invalid choice. Please try again.")

        # Exception handling hierarchy - specific to general
        except ValueError:  # Handle invalid number conversions
            print("Please enter a valid number.")
        except IndexError:  # Handle invalid list indices
            print("Please enter a valid number.")
        except Exception as e:  # Handle any other unexpected errors
            print(f"An error occurred: {e} Please try again.")

# =============================================================================
# PROGRAM ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    """
    Program entry point - only runs when script is executed directly.

    This pattern ensures the main() function only runs when this file
    is executed as a script, not when imported as a module.
    """
    main()