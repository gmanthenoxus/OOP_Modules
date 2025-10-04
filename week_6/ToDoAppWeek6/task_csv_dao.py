"""
Task CSV DAO Module - Week 6 Data Persistence

Demonstrates CSV-based Data Access Object implementation:
- Persistent storage using CSV format
- File I/O operations for task data
- Data serialization and deserialization
- UML class diagram implementation (TaskCsvDAO)

Author: [MOSES GANA]
"""

import csv
import datetime
from task import Task, RecurringTask


class TaskCsvDAO:
    """CSV Data Access Object for persistent task storage."""

    def __init__(self, storage_path: str) -> None:
        """Initialize CSV DAO with file path."""
        self.storage_path = storage_path
    
    def save_all_tasks(self, tasks: list[Task]) -> None:
        """Save all tasks to CSV file using DictWriter."""
        fieldnames = ["title", "type", "date_due", "completed", "interval", "completed_dates", "date_created"]

        try:
            with open(self.storage_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                for task in tasks:
                    row = {"title": task.title}

                    if isinstance(task, RecurringTask):
                        row["type"] = "RecurringTask"
                        row["interval"] = str(task.interval.days)
                        row["completed_dates"] = ','.join([
                            date.strftime("%Y-%m-%d") for date in task.completed_dates
                        ])
                    else:
                        row["type"] = "Task"
                        row["interval"] = ""
                        row["completed_dates"] = ""

                    row["date_due"] = task.date_due.strftime("%Y-%m-%d")
                    row["completed"] = str(task.completed)
                    row["date_created"] = task.date_created.strftime("%Y-%m-%d")

                    writer.writerow(row)

            print(f"Saved {len(tasks)} tasks to {self.storage_path}")

        except Exception as e:
            print(f"Error saving tasks to {self.storage_path}: {e}")
    
    def get_all_tasks(self) -> list[Task]:
        """Load all tasks from CSV file using DictReader."""
        task_list = []

        try:
            with open(self.storage_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    try:
                        # Parse basic task data
                        date_due = datetime.datetime.strptime(row["date_due"], "%Y-%m-%d")
                        date_created = datetime.datetime.strptime(row["date_created"], "%Y-%m-%d")
                        completed = row["completed"].lower() == 'true'

                        # Create task based on type
                        if row["type"] == "RecurringTask":
                            interval_days = int(row["interval"]) if row["interval"] else 7
                            interval = datetime.timedelta(days=interval_days)
                            task = RecurringTask(row["title"], date_due, interval)

                            # Parse completed dates
                            if row["completed_dates"]:
                                task.completed_dates = []
                                for date_str in row["completed_dates"].split(','):
                                    if date_str.strip():
                                        completed_date = datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")
                                        task.completed_dates.append(completed_date)
                        else:
                            task = Task(row["title"], date_due)

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
