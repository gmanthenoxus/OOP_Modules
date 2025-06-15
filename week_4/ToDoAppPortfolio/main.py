"""
Enhanced Main Application - Portfolio To-Do List Manager
========================================================

This is the main entry point for the enhanced portfolio To-Do application.
It demonstrates professional-level features and implementation:
- Enhanced user interface with additional menu options
- Advanced task management (overdue task filtering)
- Comprehensive error handling and user experience
- Professional code organization and documentation
- Extended functionality (task descriptions)
- Portfolio-quality implementation standards

Enhanced Features:
- Task descriptions for detailed task information
- Overdue task filtering and management
- Enhanced editing capabilities
- Professional user interface design
- Comprehensive error handling

Module Dependencies:
- tasklist.py: Enhanced TaskList class with overdue functionality
- task.py: Enhanced Task class with description support
- datetime: Python standard library for date/time operations

Author: [Student Name]
Date: [Date]
"""

# =============================================================================
# IMPORTS - ENHANCED MODULE DEPENDENCIES
# =============================================================================

from tasklist import TaskList  # Import enhanced TaskList class
import datetime  # Python standard library for date/time operations
from task import Task  # Import enhanced Task class with description support

# =============================================================================
# MAIN APPLICATION FUNCTION - PORTFOLIO VERSION
# =============================================================================

def main() -> None:
    """
    Main application function for the enhanced portfolio To-Do list manager.

    This enhanced version demonstrates:
    - Professional application initialization
    - Advanced menu systems with extended functionality
    - Enhanced user experience with descriptions
    - Comprehensive error handling and validation
    - Professional code organization and documentation
    - Portfolio-quality implementation standards

    Enhanced Features:
    - Task descriptions for detailed information
    - Overdue task filtering and management
    - Enhanced editing capabilities (title, date, description)
    - Professional user interface design

    Returns:
        None: Function runs until user chooses to quit
    """
    # Enhanced application initialization
    input_owner = input("Enter the name of the owner: ")
    task_list = TaskList(input_owner)  # Create enhanced TaskList instance
    print(f"Welcome {task_list.owner}")  # Professional welcome message

    # Enhanced main application loop with comprehensive error handling
    while True:
        try:
            # Enhanced menu with additional options
            print("\nTo-Do List Manager - Portfolio Edition")
            print("1. Add a task")
            print("2. View tasks")
            print("3. View overdue tasks")  # Enhanced feature
            print("4. Remove a task")
            print("5. Mark task as completed")
            print("6. Edit task")  # Enhanced with description editing
            print("7. Quit")

            choice = input("Enter your choice: ")  # Get user selection

            if choice == "1":  # Add a new enhanced task with description
                title = input("Enter the task you want to add:  ")
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")

                # Enhanced feature: Optional task description
                add_description = input("Would you like to add a description? (y/n): ")
                if add_description.lower() == "y":
                    description = input("Enter the description: ")
                else:
                    description = "No Description Provided"  # Fixed typo

                # Create enhanced Task instance with description
                task = Task(title, date_object, description)
                task_list.add_task(task)

            elif choice == "2":  # View all tasks
                task_list.view_tasks()

            elif choice == "3":  # Enhanced feature: View overdue tasks
                task_list.view_overdue_tasks()

            elif choice == "4":  # Remove a task
                task_list.view_tasks()  # Show tasks first
                if not task_list.tasks:  # Check if list is empty
                    continue
                else:
                    ix = int(input("Enter the task number to remove: "))
                    task_list.remove_task(ix - 1)  # Convert to 0-based index

            elif choice == "5":  # Mark task as completed
                task_list.view_tasks()  # Show tasks first
                if not task_list.tasks:  # Check if list is empty
                    continue
                else:
                    completed = int(input("Enter the task number to mark as completed: "))
                    task_list.tasks[completed - 1].mark_as_completed()

            elif choice == "6":  # Enhanced editing with description support
                task_list.view_tasks()  # Show tasks first
                if not task_list.tasks:  # Check if list is empty
                    continue
                else:
                    title_num = int(input("Enter the task to Edit: "))
                    # Validate task number is within range
                    if 1 <= title_num <= len(task_list.tasks):
                        # Enhanced editing options including description
                        edit = input("Do you want to edit the title(t), due date(dd) or description(d)? (title/date/description): ").lower()

                        if edit == "title" or edit == "t":  # Edit title
                            new_title = input("Enter the new title: ")
                            task_list.tasks[title_num - 1].change_title(new_title)

                        elif edit == "date" or edit == "dd":  # Edit date
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            task_list.tasks[title_num - 1].change_date(date_object)

                        elif edit == "description" or edit == "d":  # Enhanced: Edit description
                            new_description = input("Enter the new description: ")
                            task_list.tasks[title_num - 1].change_description(new_description)

                        else:  # Invalid edit choice
                            print("Invalid choice. Please try again.")
                            continue
                    else:  # Invalid task number
                        print("Invalid task number.")

            elif choice == "7":  # Quit application
                print("Exiting program. Goodbye!")
                break  # Exit the main loop

            else:  # Invalid menu choice
                print("Invalid choice. Please try again.")

        # Enhanced exception handling hierarchy
        except ValueError:  # Handle invalid number conversions and date parsing
            print("Please enter a valid number or date format (YYYY-MM-DD).")
        except IndexError:  # Handle invalid list indices
            print("Please enter a valid task number.")
        except Exception as e:  # Handle any other unexpected errors
            print(f"An error occurred: {e} Please try again.")

# =============================================================================
# PROGRAM ENTRY POINT - PORTFOLIO VERSION
# =============================================================================

if __name__ == "__main__":
    """
    Program entry point for the portfolio To-Do application.

    This ensures the main() function only runs when this file
    is executed directly, not when imported as a module.
    """
    main()