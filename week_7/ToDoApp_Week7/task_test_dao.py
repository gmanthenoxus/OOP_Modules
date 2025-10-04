"""
Task Test DAO Module - Week 6

This module implements a test Data Access Object (DAO) for the Task system.
It demonstrates the DAO pattern for data persistence without actual file I/O.
This is useful for testing and development purposes.

The DAO pattern provides:
- Abstraction of data storage implementation
- Consistent interface for data operations
- Easy switching between different storage methods
- Separation of concerns between business logic and data access

Classes:
- TaskTestDAO: Test implementation that returns hardcoded data

Author: [GLORY TITILOPE OLANREWAJU]
"""


# IMPORTS


import datetime  # For creating test dates
from task import Task, RecurringTask  # Import Task classes


# TASK TEST DAO CLASS DEFINITION


class TaskTestDAO:
    """
    Test Data Access Object for Task persistence.
    
    This class provides a test implementation of the DAO pattern
    that returns hardcoded test data instead of reading from files.
    It's useful for testing and development without file dependencies.
    
    Attributes:
        storage_path (str): Path where data would be stored (for interface consistency)
    """
    
    def __init__(self, storage_path: str = "test_data") -> None:
        """
        Initialize the test DAO with a storage path.
        
        Args:
            storage_path (str): Path identifier (not used in test implementation)
            
        Returns:
            None: Constructors don't return values
        """
        self.storage_path = storage_path
    
    def get_all_tasks(self) -> list[Task]:
        """
        Retrieve all tasks from test data (Exercise 1 implementation).

        This method returns a predefined set of test tasks exactly as specified
        in the exercise requirements, simulating loading from persistent storage.

        Returns:
            list[Task]: A list of test Task objects
        """
        # Create task list exactly as specified in Exercise 1
        task_list = [
            Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)),
            Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2)),
            Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1)),
            Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)),
            Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)),
            Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))
        ]

        # Sample recurring task as specified in Exercise 1
        r_task = RecurringTask("Go to the gym", datetime.datetime.now(), datetime.timedelta(days=7))

        # Propagate the recurring task with some completed dates
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
        r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)

        task_list.append(r_task)

        print(f"Loaded {len(task_list)} test tasks from {self.storage_path}")
        return task_list
    
    def save_all_tasks(self, tasks: list[Task]) -> None:
        """
        Save all tasks (test implementation - no actual saving).
        
        This method simulates saving tasks to persistent storage.
        In the test implementation, it just prints confirmation.
        
        Args:
            tasks (list[Task]): List of tasks to save
            
        Returns:
            None: Method simulates saving but doesn't return a value
            
        Example:
            >>> dao = TaskTestDAO()
            >>> dao.save_all_tasks(task_list)
            Simulated saving 3 tasks to test_data
        """
        print(f"Simulated saving {len(tasks)} tasks to {self.storage_path}")
        
        # In a real implementation, this would write to a file or database
        # For testing, we just confirm the operation
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task.title} - {'Completed' if task.completed else 'Not Completed'}")
