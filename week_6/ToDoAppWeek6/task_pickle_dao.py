"""
Task Pickle DAO Module - Week 6 (Optional Exercise 3)

This module implements a Pickle-based Data Access Object (DAO) for the Task system.
It demonstrates serialization using Python's pickle module, which can serialize
complete Python objects without needing to handle individual attributes.

The Pickle DAO provides:
- Complete object serialization/deserialization
- Simpler implementation than CSV
- Preserves exact object state
- Binary file format (not human-readable)

Classes:
- TaskPickleDAO: Pickle file implementation for task persistence

Author: [Moses Gana]
"""


# IMPORTS


import pickle  # For object serialization
from task import Task, RecurringTask  # Import Task classes


# TASK PICKLE DAO CLASS DEFINITION


class TaskPickleDAO:
    """
    Pickle Data Access Object for Task persistence.
    
    This class provides pickle-based implementation of the DAO pattern
    for storing and retrieving tasks. It uses Python's pickle module
    to serialize complete task objects to binary files.
    
    Attributes:
        storage_path (str): Path to the pickle file for data storage
    """
    
    def __init__(self, storage_path: str) -> None:
        """
        Initialize the Pickle DAO with a file path.
        
        Args:
            storage_path (str): Path to the pickle file for task storage
            
        Returns:
            None: Constructors don't return values
            
        Example:
            >>> dao = TaskPickleDAO("tasks.pkl")
        """
        self.storage_path = storage_path
    
    def save_all_tasks(self, tasks: list[Task]) -> None:
        """
        Save all tasks to pickle file.
        
        This method serializes the entire list of task objects to a binary
        pickle file. This preserves the complete object state including
        all attributes and methods.
        
        Args:
            tasks (list[Task]): List of tasks to save to pickle file
            
        Returns:
            None: Method writes to file but doesn't return a value
            
        Example:
            >>> dao = TaskPickleDAO("tasks.pkl")
            >>> dao.save_all_tasks(task_list.tasks)
            Saved 3 tasks to tasks.pkl using pickle
        """
        try:
            with open(self.storage_path, 'wb') as file:
                # Serialize the entire task list to binary file
                pickle.dump(tasks, file)
            
            print(f"Saved {len(tasks)} tasks to {self.storage_path} using pickle")
            
        except Exception as e:
            print(f"Error saving tasks to {self.storage_path}: {e}")
    
    def get_all_tasks(self) -> list[Task]:
        """
        Load all tasks from pickle file.
        
        This method deserializes the complete list of task objects from
        a binary pickle file. This restores the exact object state that
        was saved, including all attributes and methods.
        
        Returns:
            list[Task]: List of tasks loaded from pickle file
            
        Example:
            >>> dao = TaskPickleDAO("tasks.pkl")
            >>> tasks = dao.get_all_tasks()
            >>> print(f"Loaded {len(tasks)} tasks using pickle")
        """
        tasks = []
        
        try:
            with open(self.storage_path, 'rb') as file:
                # Deserialize the entire task list from binary file
                tasks = pickle.load(file)
            
            print(f"Loaded {len(tasks)} tasks from {self.storage_path} using pickle")
            
        except FileNotFoundError:
            print(f"No existing pickle file found at {self.storage_path}. Starting with empty task list.")
        except Exception as e:
            print(f"Error loading tasks from {self.storage_path}: {e}")
        
        return tasks
