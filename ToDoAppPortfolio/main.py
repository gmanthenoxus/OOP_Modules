"""
ToDoApp Portfolio - Comprehensive OOP Implementation

Demonstrates complete OOP curriculum integration:
- Abstract base classes with @abstractmethod decorator (Week 8)
- SOLID principles and Factory pattern (Week 7)
- Data persistence with DAO pattern (Week 6)
- Inheritance and polymorphism (Week 5)
- Classes, objects, and encapsulation (Week 4)
- Priority task management and user roles
- Professional architecture and error handling

Author: [IKENNA FRAKLIN EZEMA]
"""

from ui import CommandLineUI


def main() -> None:
    """Main application demonstrating comprehensive OOP concepts integration."""
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
    # Enhanced application initialization with Owner class
    input_name = input("Enter the name of the owner: ")
    input_email = input("Enter the owner's email: ")
    owner = Owner(input_name, input_email)  # Create Owner instance
    task_list = TaskList(owner)  # Create enhanced TaskList instance with Owner
    print(f"Welcome {owner.name}")  # Professional welcome message
    print(f"Owner Details: {owner}")  # Display owner information

    # Add sample recurring task for demonstration
    sample_recurring = RecurringTask(
        "Weekly Review",
        datetime.datetime.now() + datetime.timedelta(days=7),
        "Review weekly goals and progress",
        datetime.timedelta(days=7)
    )
    task_list.add_task(sample_recurring)

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
            print("7. Add recurring task")  # New: Add recurring task feature
            print("8. Quit")

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
                    try:
                        # Use encapsulation - get_task method instead of direct access
                        task = task_list.get_task(completed - 1)
                        task.mark_as_completed()
                    except IndexError:
                        print("Please enter a valid task number.")

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
                            try:
                                # Use encapsulation - get_task method instead of direct access
                                task = task_list.get_task(title_num - 1)
                                task.change_title(new_title)
                            except IndexError:
                                print("Please enter a valid task number.")

                        elif edit == "date" or edit == "dd":  # Edit date
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            try:
                                # Use encapsulation - get_task method instead of direct access
                                task = task_list.get_task(title_num - 1)
                                task.change_date(date_object)
                            except IndexError:
                                print("Please enter a valid task number.")

                        elif edit == "description" or edit == "d":  # Enhanced: Edit description
                            new_description = input("Enter the new description: ")
                            try:
                                # Use encapsulation - get_task method instead of direct access
                                task = task_list.get_task(title_num - 1)
                                task.change_description(new_description)
                            except IndexError:
                                print("Please enter a valid task number.")

                        else:  # Invalid edit choice
                            print("Invalid choice. Please try again.")
                            continue
                    else:  # Invalid task number
                        print("Invalid task number.")

            elif choice == "7":  # Add recurring task
                title = input("Enter the recurring task title: ")
                input_date = input("Enter the first due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                description = input("Enter the task description: ")

                # Get interval for recurring task
                print("Select interval:")
                print("1. Daily")
                print("2. Weekly")
                print("3. Monthly")
                print("4. Custom (days)")

                interval_choice = input("Enter interval choice: ")

                if interval_choice == "1":
                    interval = datetime.timedelta(days=1)
                elif interval_choice == "2":
                    interval = datetime.timedelta(days=7)
                elif interval_choice == "3":
                    interval = datetime.timedelta(days=30)
                elif interval_choice == "4":
                    days = int(input("Enter number of days: "))
                    interval = datetime.timedelta(days=days)
                else:
                    print("Invalid choice, defaulting to weekly.")
                    interval = datetime.timedelta(days=7)

                recurring_task = RecurringTask(title, date_object, description, interval)
                task_list.add_task(recurring_task)
                print(f"Recurring task '{title}' added successfully!")

            elif choice == "8":  # Quit application
                print("Exiting program. Goodbye!")
                print(f"Final owner details: {owner}")
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


# PROGRAM ENTRY POINT - PORTFOLIO VERSION


if __name__ == "__main__":
    """
    Program entry point for the portfolio To-Do application.

    This ensures the main() function only runs when this file
    is executed directly, not when imported as a module.
    """
    main()


