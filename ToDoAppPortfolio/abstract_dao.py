"""
Abstract DAO Module - Portfolio Implementation

Demonstrates abstract classes and Dependency Inversion Principle:
- AbstractDAO with @abstractmethod decorator (Week 8)
- Consistent interface across storage mechanisms (Week 6)
- Support for all task types including PriorityTask
- Polymorphic behavior for different storage backends

Author: [IKENNA FRAKLIN EZEMA]
"""

import csv
import datetime
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from task import AbstractTask, Task, RecurringTask, PriorityTask


class AbstractDAO(ABC):
    """Abstract base class for all DAO implementations - demonstrates Week 8 concepts."""

    def __init__(self, storage_path: str) -> None:
        """
        Initialize DAO with storage path.
        
        Args:
            storage_path: Path to the data storage location
        """
        self.storage_path = storage_path
    
    @abstractmethod
    def get_all_tasks(self) -> List[AbstractTask]:
        """
        Abstract method to retrieve all tasks from storage.
        
        Returns:
            List[AbstractTask]: List of all tasks from storage
        """
        pass
    
    @abstractmethod
    def save_all_tasks(self, tasks: List[AbstractTask]) -> None:
        """
        Abstract method to save all tasks to storage.
        
        Args:
            tasks: List of tasks to save
        """
        pass
    
    def get_storage_info(self) -> str:
        """Get information about the storage location (common implementation)."""
        return f"{self.__class__.__name__} using: {self.storage_path}"


# TEST DAO IMPLEMENTATION


class TaskTestDAO(AbstractDAO):
    """
    Test DAO implementation for development and testing.
    
    This class provides a concrete implementation of the abstract DAO
    that returns predefined test data including all task types.
    """
    
    def get_all_tasks(self) -> List[AbstractTask]:
        """
        Get predefined test tasks including all task types.
        
        Returns:
            List[AbstractTask]: List of test tasks
        """
        # Create test tasks using all available task types
        tasks = [
            Task("Buy groceries", datetime.datetime.now() + datetime.timedelta(days=1), 
                 "Weekly grocery shopping"),
            Task("Complete assignment", datetime.datetime.now() + datetime.timedelta(days=3),
                 "Finish the programming assignment"),
            RecurringTask("Weekly team meeting", datetime.datetime.now() + datetime.timedelta(days=2),
                         datetime.timedelta(days=7), "Regular team sync meeting"),
            PriorityTask("Important client call", datetime.datetime.now() + datetime.timedelta(hours=4),
                        3, "High priority client discussion"),
            PriorityTask("Review documents", datetime.datetime.now() + datetime.timedelta(days=2),
                        2, "Medium priority document review"),
            PriorityTask("Organize desk", datetime.datetime.now() + datetime.timedelta(days=5),
                        1, "Low priority office organization")
        ]
        
        print(f"Loaded {len(tasks)} test tasks from {self.storage_path}")
        return tasks
    
    def save_all_tasks(self, tasks: List[AbstractTask]) -> None:
        """
        Simulate saving tasks (test implementation).
        
        Args:
            tasks: List of tasks to save
        """
        print(f"Simulated saving {len(tasks)} tasks to {self.storage_path}")
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task.completed else "Not Completed"
            task_type = task.get_task_type()
            priority_info = ""
            if isinstance(task, PriorityTask):
                priority_info = f" (Priority: {task.get_priority_string()})"
            print(f"  {i}. {task.title} - {task_type} - {status}{priority_info}")


# CSV DAO IMPLEMENTATION


class TaskCsvDAO(AbstractDAO):
    """
    CSV file DAO implementation for persistent storage.
    
    This class provides concrete implementation of the abstract DAO
    that reads from and writes to CSV files, supporting all task types
    including the new PriorityTask.
    """
    
    def __init__(self, storage_path: str) -> None:
        """Initialize CSV DAO with file path."""
        super().__init__(storage_path)
        # Define fieldnames for CSV structure including priority support
        self.fieldnames = [
            "title", "type", "date_due", "completed", "interval", 
            "completed_dates", "date_created", "description", "priority_level"
        ]
    
    def get_all_tasks(self) -> List[AbstractTask]:
        """
        Load all tasks from CSV file including PriorityTask support.
        
        Returns:
            List[AbstractTask]: List of tasks loaded from CSV file
        """
        task_list = []
        
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    try:
                        # Parse common task data
                        task_type = row["type"]
                        task_title = row["title"]
                        task_date_due = row["date_due"]
                        task_completed = row["completed"]
                        task_date_created = row["date_created"]
                        task_description = row.get("description", "")
                        
                        # Parse dates
                        date_due = datetime.datetime.strptime(task_date_due, "%Y-%m-%d")
                        date_created = datetime.datetime.strptime(task_date_created, "%Y-%m-%d")
                        completed = task_completed.lower() == 'true'
                        
                        # Create task based on type
                        if task_type == "PriorityTask":
                            # Parse priority level
                            priority_level = int(row["priority_level"])
                            task = PriorityTask(task_title, date_due, priority_level, task_description)
                            
                        elif task_type == "RecurringTask":
                            # Parse interval and completed dates
                            task_interval = row["interval"]
                            task_completed_dates = row["completed_dates"]
                            
                            interval_days = int(task_interval.split()[0]) if task_interval else 7
                            interval = datetime.timedelta(days=interval_days)
                            
                            task = RecurringTask(task_title, date_due, interval, task_description)
                            
                            # Parse completed dates list
                            if task_completed_dates:
                                completed_dates_list = task_completed_dates.split(',')
                                task.completed_dates = []
                                for date_str in completed_dates_list:
                                    if date_str.strip():
                                        completed_date = datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")
                                        task.completed_dates.append(completed_date)
                        else:
                            # Create regular task
                            task = Task(task_title, date_due, task_description)
                        
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
    
    def save_all_tasks(self, tasks: List[AbstractTask]) -> None:
        """
        Save all tasks to CSV file including PriorityTask support.
        
        Args:
            tasks: List of tasks to save to CSV
        """
        try:
            with open(self.storage_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.fieldnames)
                writer.writeheader()
                
                for task in tasks:
                    row = {}
                    
                    # Common fields
                    row["title"] = task.title
                    row["type"] = task.get_task_type()
                    row["date_due"] = task.date_due.strftime("%Y-%m-%d")
                    row["completed"] = str(task.completed)
                    row["date_created"] = task.date_created.strftime("%Y-%m-%d")
                    row["description"] = task.description
                    
                    # Type-specific fields
                    if isinstance(task, PriorityTask):
                        row["priority_level"] = str(task.priority_level)
                        row["interval"] = ""
                        row["completed_dates"] = ""
                        
                    elif isinstance(task, RecurringTask):
                        row["priority_level"] = ""
                        row["interval"] = str(task.interval.days)
                        row["completed_dates"] = ','.join([
                            date.strftime("%Y-%m-%d") for date in task.completed_dates
                        ])
                        
                    else:  # Regular Task
                        row["priority_level"] = ""
                        row["interval"] = ""
                        row["completed_dates"] = ""
                    
                    writer.writerow(row)
            
            print(f"Saved {len(tasks)} tasks to {self.storage_path}")
            
        except Exception as e:
            print(f"Error saving tasks to {self.storage_path}: {e}")
