"""
Enhanced Main Application - Week 5 OOP Concepts

Demonstrates inheritance, polymorphism, and encapsulation:
- RecurringTask inheritance from Task
- Polymorphic mark_as_completed method
- Encapsulated task access via get_task method
- Enhanced user interface with recurring task support

Author: [VICTOR NNAMDI EKWEMALOR]
"""

from tasklist import TaskList
import datetime
from task import Task, RecurringTask




def main() -> None:
    """Main application demonstrating OOP concepts."""
    input_owner = input("Enter the name of the owner: ")
    task_list = TaskList(input_owner)
    print(f"Welcome {task_list.owner}")

    # Create sample recurring task
    r_task = RecurringTask("Go to the gym", datetime.datetime.now() + datetime.timedelta(days=1), datetime.timedelta(days=7))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
    r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
    r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)
    task_list.add_task(r_task)

    while True:
        try:
            print("\nTo-Do List Manager")
            print("1. Add a task")
            print("2. View tasks")
            print("3. View overdue tasks")
            print("4. Remove a task")
            print("5. Mark task as completed")
            print("6. Edit task")
            print("7. Quit")

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

            elif choice == "2":
                task_list.view_tasks()

            elif choice == "3":
                task_list.view_overdue_tasks()

            elif choice == "4":
                task_list.view_tasks()
                if not task_list.tasks:
                    continue
                else:
                    ix = int(input("Enter the task number to remove: "))
                    task_list.remove_task(ix - 1)

            elif choice == "5":
                task_list.view_tasks()
                if not task_list.tasks:
                    continue
                else:
                    completed = int(input("Enter the task number to mark as completed: "))
                    try:
                        # Demonstrates encapsulation
                        task = task_list.get_task(completed - 1)
                        task.mark_as_completed()  # Polymorphic method call
                    except IndexError:
                        print("Please enter a valid task number.")

            elif choice == "6":
                task_list.view_tasks()
                if not task_list.tasks:
                    continue
                else:
                    title_num = int(input("Enter the task to Edit: "))
                    if 1 <= title_num <= len(task_list.tasks):
                        edit = input("Do you want to edit the title(t), due date(dd)? (title/date): ").lower()

                        if edit == "title" or edit == "t":
                            new_title = input("Enter the new title: ")
                            try:
                                task = task_list.get_task(title_num - 1)
                                task.change_title(new_title)
                            except IndexError:
                                print("Please enter a valid task number.")

                        elif edit == "date" or edit == "dd":
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            try:
                                task = task_list.get_task(title_num - 1)
                                task.change_date(date_object)
                            except IndexError:
                                print("Please enter a valid task number.")

                        else:
                            print("Invalid choice. Please try again.")
                            continue
                    else:
                        print("Invalid task number.")

            elif choice == "7":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter a valid number or date format (YYYY-MM-DD).")
        except IndexError:
            print("Please enter a valid task number.")
        except Exception as e:
            print(f"An error occurred: {e} Please try again.")


if __name__ == "__main__":
    main()

