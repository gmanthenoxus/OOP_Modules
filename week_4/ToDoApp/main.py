"""
Main Application - Modularized To-Do List Manager

Entry point for the modularized To-Do application demonstrating:
- Module imports and organization
- Function-based program structure
- Comprehensive error handling
- Interactive menu systems

Author: [VICTOR USMAN]
"""

from task_list import TaskList
import datetime
from task import Task


def propagate_task_list(task_list: TaskList) -> TaskList:
    """Populate task list with sample tasks for testing."""
    task_list.add_task(Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)))
    task_list.add_task(Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2)))
    task_list.add_task(Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1)))
    task_list.add_task(Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)))
    task_list.add_task(Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)))
    task_list.add_task(Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6)))
    return task_list

def main() -> None:
    """Main application function with interactive menu system."""
    input_owner = input("Enter the name of the owner: ")
    task_list = TaskList(input_owner)

    # Uncomment to populate with sample data for testing
    # task_list = propagate_task_list(task_list)

    print(f"Welcome {task_list.owner}")

    while True:
        try:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. Remove a task")
            print("4. Mark task as completed")
            print("5. Edit task")
            print("6. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter the task you want to add:  ")
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
                task = Task(title, date_object)
                task_list.add_task(task)

            elif choice == "2":
                task_list.view_tasks()

            elif choice == "3":
                task_list.view_tasks()
                if not task_list.tasks:
                    continue
                else:
                    ix = int(input("Enter the task number to remove: "))
                    task_list.remove_task(ix - 1)

            elif choice == "4":
                task_list.view_tasks()
                if not task_list.tasks:
                    continue
                else:
                    completed = int(input("Enter the task number to mark as completed: "))
                    task_list.tasks[completed - 1].mark_as_completed()

            elif choice == "5":
                task_list.view_tasks()
                if not task_list.tasks:
                    continue
                else:
                    title_num = int(input("Enter the task to Edit: "))
                    if 1 <= title_num <= len(task_list.tasks):
                        edit = input("Do you want to edit the title,due date or both? (title/date/both): ").lower()

                        if edit == "title" or edit == "t":
                            new_title = input("Enter the new title: ")
                            task_list.tasks[title_num - 1].change_title(new_title)

                        elif edit == "date" or edit == "d":
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            task_list.tasks[title_num - 1].change_date(date_object)

                        elif edit == "both" or edit == "b":
                            new_title = input("Enter the new title: ")
                            task_list.tasks[title_num - 1].change_title(new_title)
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            task_list.tasks[title_num - 1].change_date(date_object)

                        else:
                            print("Invalid choice. Please try again.")
                            continue
                    else:
                        print("Invalid task number.")

            elif choice == "6":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a valid number.")
        except IndexError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e} Please try again.")

if __name__ == "__main__":
    main()

