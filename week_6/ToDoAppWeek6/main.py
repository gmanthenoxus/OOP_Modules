"""
Enhanced Main Application - Week 6 Data Persistence

Demonstrates data persistence using DAO pattern:
- TaskTestDAO for in-memory testing
- TaskCsvDAO for CSV file persistence
- @property decorators for computed attributes
- Enhanced task management with persistence

Author: [MOSES GANA]
"""

from tasklist import TaskList
import datetime
from task import Task, RecurringTask
from task_test_dao import TaskTestDAO
from task_csv_dao import TaskCsvDAO
from task_pickle_dao import TaskPickleDAO




def main() -> None:
    """Main application demonstrating DAO pattern and @property decorators."""
    input_owner = input("Enter the name of the owner: ")
    task_list = TaskList(input_owner)
    print(f"Welcome {task_list.owner}")

    dao = None

    while True:
        try:
            print("\nTo-Do List Manager - Week 6 with DAO Pattern")
            print("1. Add a task")
            print("2. View tasks")
            print("3. View overdue tasks")
            print("4. Remove a task")
            print("5. Mark task as completed")
            print("6. Edit task")
            print("7. Load tasks from DAO")
            print("8. Save tasks to DAO")
            print("9. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter the task you want to add:  ")
                task_type = input("Is this a recurring task? (y/n): ").lower()
                if task_type == "y":
                    interval = input("Enter the interval (in days): ")
                    interval_object = datetime.timedelta(days=int(interval))
                elif task_type == "n":
                    interval_object = None
                else:
                    print("Invalid choice. Please try again.")
                    continue
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")

                if task_type == "y":
                    task = RecurringTask(title, date_object, interval_object)
                else:
                    task = Task(title, date_object)
                task_list.add_task(task)

            elif choice == "2":  # View all tasks
                task_list.view_tasks()

            elif choice == "3":  
                task_list.view_overdue_tasks()

            elif choice == "4":  
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

            elif choice == "6":  
                task_list.view_tasks()  # Show tasks first
                if not task_list.tasks:  # Check if list is empty
                    continue
                else:
                    title_num = int(input("Enter the task to Edit: "))
                    # Validate task number is within range
                    if 1 <= title_num <= len(task_list.tasks):
                        edit = input("Do you want to edit the title(t), due date(dd)? (title/date): ").lower()

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

                        else:  # Invalid edit choice
                            print("Invalid choice. Please try again.")
                            continue
                    else:  # Invalid task number
                        print("Invalid task number.")

            elif choice == "7":  # Load tasks from DAO
                file_path = input("Enter file path for loading tasks: ")
                dao_type = input("Use test DAO (t), CSV DAO (c), or Pickle DAO (p)? [default: c]: ").lower()

                if dao_type == 't':
                    dao = TaskTestDAO(file_path)
                    print("Using TaskTestDAO for loading...")
                elif dao_type == 'p':
                    dao = TaskPickleDAO(file_path)
                    print("Using TaskPickleDAO for loading...")
                else:
                    dao = TaskCsvDAO(file_path)
                    print("Using TaskCsvDAO for loading...")

                # Load tasks from DAO
                loaded_tasks = dao.get_all_tasks()

                # Add loaded tasks to task list one by one
                for task in loaded_tasks:
                    task_list.add_task(task)

                print(f"Successfully loaded {len(loaded_tasks)} tasks!")

            elif choice == "8":  # Save tasks to DAO
                if dao is None:
                    file_path = input("Enter file path for saving tasks: ")
                    dao_type = input("Use test DAO (t), CSV DAO (c), or Pickle DAO (p)? [default: c]: ").lower()

                    if dao_type == 't':
                        dao = TaskTestDAO(file_path)
                        print("Using TaskTestDAO for saving...")
                    elif dao_type == 'p':
                        dao = TaskPickleDAO(file_path)
                        print("Using TaskPickleDAO for saving...")
                    else:
                        dao = TaskCsvDAO(file_path)
                        print("Using TaskCsvDAO for saving...")

                # Save tasks using DAO
                dao.save_all_tasks(task_list.tasks)
                print("Tasks saved successfully!")

            elif choice == "9":  # Quit application
                if dao is not None and task_list.tasks:
                    auto_save = input("Auto-save tasks before exit? (y/n): ").lower()
                    if auto_save == 'y':
                        dao.save_all_tasks(task_list.tasks)
                        print("Tasks auto-saved!")
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


# PROGRAM ENTRY POINT


if __name__ == "__main__":
    """
    Program entry point for the To-Do application.

    This ensures the main() function only runs when this file
    is executed directly, not when imported as a module.
    """
    main()

