"""
Task CSV DAO Module - Week 6

This module implements a CSV-based Data Access Object (DAO) for the Task system.
It demonstrates persistent data storage using CSV (Comma Separated Values) format.
This provides a simple, human-readable way to store task data.

The CSV DAO provides:
- Persistent storage of task data
- Human-readable file format
- Easy data import/export capabilities
- Cross-platform compatibility

Classes:
- TaskCsvDAO: CSV file implementation for task persistence

Author: [GLORY TITILOPE OLANREWAJU]
"""


# IMPORTS


import csv  # For CSV file operations
import datetime  # For date parsing and formatting
from task import Task, RecurringTask  # Import Task classes


# TASK CSV DAO CLASS DEFINITION


class TaskCsvDAO:
    """
    CSV Data Access Object for Task persistence.
    
    This class provides CSV file-based implementation of the DAO pattern
    for storing and retrieving tasks. It handles the conversion between
    Task objects and CSV file format.
    
    Attributes:
        storage_path (str): Path to the CSV file for data storage
    """
    
    def __init__(self, storage_path: str) -> None:
        """
        Initialize the CSV DAO with a file path.
        
        Args:
            storage_path (str): Path to the CSV file for task storage
            
        Returns:
            None: Constructors don't return values
            
        Example:
            >>> dao = TaskCsvDAO("tasks.csv")
        """
        self.storage_path = storage_path
    
    def save_all_tasks(self, tasks: list[Task]) -> None:
        """
        Save all tasks to CSV file using DictWriter (Task B implementation).

        This method writes all tasks to a CSV file with proper field mapping
        and handles both Task and RecurringTask objects correctly.

        Args:
            tasks (list[Task]): List of tasks to save to CSV

        Returns:
            None: Method writes to file but doesn't return a value
        """
        # Define fieldnames for CSV structure
        fieldnames = ["title", "type", "date_due", "completed", "interval", "completed_dates", "date_created"]

        try:
            with open(self.storage_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for task in tasks:
                    row = {}

                    # Task B: Complete the save_all_tasks method
                    row["title"] = task.title

                    # Determine task type using isinstance
                    if isinstance(task, RecurringTask):
                        row["type"] = "RecurringTask"
                        # Convert interval to string (days only)
                        row["interval"] = str(task.interval.days)
                        # Join completed dates with comma separator
                        row["completed_dates"] = ','.join([
                            date.strftime("%Y-%m-%d") for date in task.completed_dates
                        ])
                    else:
                        row["type"] = "Task"
                        row["interval"] = ""  # No interval for regular tasks
                        row["completed_dates"] = ""  # No completed dates for regular tasks

                    # Convert datetime objects to strings using strftime
                    row["date_due"] = task.date_due.strftime("%Y-%m-%d")
                    row["completed"] = str(task.completed)
                    row["date_created"] = task.date_created.strftime("%Y-%m-%d")

                    writer.writerow(row)

            print(f"Saved {len(tasks)} tasks to {self.storage_path}")

        except Exception as e:
            print(f"Error saving tasks to {self.storage_path}: {e}")
    
    def get_all_tasks(self) -> list[Task]:
        """
        Load all tasks from CSV file using DictReader (Task A implementation).

        This method reads tasks from a CSV file and converts them back
        to Task or RecurringTask objects based on the stored data.

        Returns:
            list[Task]: List of tasks loaded from CSV file
        """
        task_list = []

        try:
            with open(self.storage_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    try:
                        # Task A: Complete the get_all_tasks method
                        task_type = row["type"]
                        task_title = row["title"]
                        task_date_due = row["date_due"]
                        task_completed = row["completed"]
                        task_interval = row["interval"]
                        task_date_created = row["date_created"]
                        task_completed_dates = row["completed_dates"]

                        # Parse the due date using strptime
                        date_due = datetime.datetime.strptime(task_date_due, "%Y-%m-%d")

                        # Parse the created date
                        date_created = datetime.datetime.strptime(task_date_created, "%Y-%m-%d")

                        # Parse completed status
                        completed = task_completed.lower() == 'true'

                        # Create task based on type using conditional
                        if task_type == "RecurringTask":
                            # Parse interval (only first number using split)
                            interval_days = int(task_interval.split()[0]) if task_interval else 7
                            interval = datetime.timedelta(days=interval_days)

                            # Create recurring task
                            task = RecurringTask(task_title, date_due, interval)

                            # Parse completed dates list using split and loop
                            if task_completed_dates:
                                completed_dates_list = task_completed_dates.split(',')
                                task.completed_dates = []
                                for date_str in completed_dates_list:
                                    if date_str.strip():  # Check if not empty
                                        completed_date = datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")
                                        task.completed_dates.append(completed_date)
                        else:
                            # Create regular task
                            task = Task(task_title, date_due)

                        # Set common properties
                        task.date_created = date_created
                        task.completed = completed

                        task_list.append(task)

                    except (ValueError, KeyError) as e:
                        print(f"Error parsing task row: {e}")
                        continue

            print(f"Loaded {len(task_list)} tasks from {self.storage_path}")

        except FileNotFoundError:
            print(f"No existing task file found at {self.storage_path}. Starting with empty task list.")
        except Exception as e:
            print(f"Error loading tasks from {self.storage_path}: {e}")

        return task_list
