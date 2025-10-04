"""
Week 4 Lab - Object-Oriented Programming and Classes

Demonstrates fundamental OOP concepts:
- Class definition and instantiation
- Constructor methods and instance variables
- Method parameters with type hints
- Interactive menu systems and error handling

Author: [VICTOR USMAN]
"""

import datetime


class TaskList:
    """Task list with owner and collection of tasks."""

    def __init__(self, owner: str) -> None:
        """Initialize TaskList with owner name."""
        self.owner = owner.title()
        self.tasks = []

    def add_task(self, task: 'Task') -> None:
        """Add task to the list."""
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def remove_task(self, ix: int) -> None:
        """Remove task by index with error handling."""
        try:
            my_task = self.tasks[ix]
            del self.tasks[ix]
            print(f"Task '{my_task}' removed.")
        except IndexError:
            print("Please enter a valid number.")

    def view_tasks(self) -> None:
        """Display all tasks with numbering."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Current tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def list_options(self) -> None:
        """Interactive menu system for task management."""
        while True:
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
                self.add_task(task)

            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.view_tasks()
                if not self.tasks:
                    continue
                else:
                    ix = int(input("Enter the task number to remove: "))
                    self.remove_task(ix - 1)

            elif choice == "4":
                self.view_tasks()
                if not self.tasks:
                    continue
                else:
                    completed = int(input("Enter the task number to mark as completed: "))
                    self.tasks[completed - 1].mark_as_completed()

            elif choice == "5":
                self.view_tasks()
                if not self.tasks:
                    continue
                else:
                    title_num = int(input("Enter the task to Edit: "))
                    if 1 <= title_num <= len(self.tasks):
                        edit = input("Do you want to edit the title,due date or both? (title/date/both): ").lower()

                        if edit == "title" or edit == "t":
                            new_title = input("Enter the new title: ")
                            self.tasks[title_num - 1].change_title(new_title)

                        elif edit == "date" or edit == "d":
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            self.tasks[title_num - 1].date_due = date_object

                        elif edit == "both" or edit == "b":
                            new_title = input("Enter the new title: ")
                            self.tasks[title_num - 1].change_title(new_title)
                            new_date = input("Enter the new due date (YYYY-MM-DD): ")
                            date_object = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                            self.tasks[title_num - 1].date_due = date_object

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

class Task:
    """Individual task with title, dates, and completion status."""

    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        """Initialize Task with title and due date."""
        self.title = title
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.completed = False

    def __str__(self) -> str:
        """Return formatted string representation of task."""
        status = "[Completed]" if self.completed else "[Not Completed]"
        return f"{self.title} {status} Created: {self.date_created} Due: {self.date_due}"

    def mark_as_completed(self) -> None:
        """Mark task as completed."""
        self.completed = True
        print(f"Task '{self.title}' is completed.")

    def change_title(self, new_title: str) -> None:
        """Change task title."""
        self.title = new_title
        print(f"Task title changed to '{self.title}'")

# Main program execution
input_owner = input("Enter the name of the owner: ")
task_list = TaskList(input_owner)
print(f"Welcome {task_list.owner}")
task_list.list_options()
