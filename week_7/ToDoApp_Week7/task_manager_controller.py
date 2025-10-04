"""
Task Manager Controller Module - Week 7 SOLID Principles

Demonstrates separation of concerns and SOLID principles:
- Single Responsibility Principle (only handles business logic)
- Dependency Inversion Principle (depends on abstractions)
- Separation of concerns (business logic separated from UI)
- Exception handling with try-except blocks

Author: [GLORY TITILOPE OLANREWAJU]
"""

import datetime
from typing import Optional, Any
from tasklist import TaskList
from task import Task, RecurringTask
from task_factory import TaskFactory
from task_test_dao import TaskTestDAO
from task_csv_dao import TaskCsvDAO
from task_pickle_dao import TaskPickleDAO


class TaskManagerController:
    """
    Controller class demonstrating SOLID principles and separation of concerns.

    - Single Responsibility: Only handles business logic
    - Dependency Inversion: Depends on abstractions, not concrete classes
    - Exception handling: Comprehensive try-except blocks
    """

    def __init__(self, owner: str) -> None:
        """Initialize controller with task list owner."""
        self.task_list = TaskList(owner)
        self.dao: Optional[Any] = None
    
    def create_task(self, title: str, due_date: datetime.datetime,
                   is_recurring: bool = False, interval_days: int = 7) -> bool:
        """Create task using Factory pattern with exception handling."""
        try:
            if is_recurring:
                interval = datetime.timedelta(days=interval_days)
                task = TaskFactory.create_task(title, due_date, interval=interval)
            else:
                task = TaskFactory.create_task(title, due_date)

            self.task_list.add_task(task)
            return True
        except Exception as e:
            print(f"Error creating task: {e}")
            return False
    
    def get_uncompleted_tasks(self) -> list[Task]:
        """Get uncompleted tasks using @property decorator."""
        return self.task_list.uncompleted_tasks

    def get_all_tasks(self) -> list[Task]:
        """Get all tasks in the task list."""
        return self.task_list.tasks

    def get_overdue_tasks(self) -> list[Task]:
        """Get all overdue tasks with date comparison logic."""
        overdue_tasks = []
        current_time = datetime.datetime.now()

        for task in self.task_list.tasks:
            if task.date_due < current_time and not task.completed:
                overdue_tasks.append(task)

        return overdue_tasks
    
    def mark_task_completed(self, task_index: int) -> tuple[bool, str]:
        """
        Mark a task as completed with proper error handling.
        
        Args:
            task_index (int): Index of task to mark as completed (1-based)
            
        Returns:
            tuple[bool, str]: (Success status, Message)
        """
        try:
            # Convert to 0-based index
            index = task_index - 1
            
            # Check if index is valid using the DRY principle method
            if not self.task_list.check_task_index(index):
                return False, "Invalid task number. Please try again."
            
            # Get and mark task as completed
            task = self.task_list.get_task(index)
            task.mark_as_completed()
            
            return True, f"Task '{task.title}' marked as completed."
            
        except Exception as e:
            return False, f"Error marking task as completed: {e}"
    
    def remove_task(self, task_index: int) -> tuple[bool, str]:
        """
        Remove a task with proper error handling.
        
        Args:
            task_index (int): Index of task to remove (1-based)
            
        Returns:
            tuple[bool, str]: (Success status, Message)
        """
        try:
            # Convert to 0-based index
            index = task_index - 1
            
            # Check if index is valid
            if not self.task_list.check_task_index(index):
                return False, "Invalid task number. Please try again."
            
            # Remove task
            self.task_list.remove_task(index)
            return True, "Task removed successfully."
            
        except Exception as e:
            return False, f"Error removing task: {e}"
    
    def edit_task_title(self, task_index: int, new_title: str) -> tuple[bool, str]:
        """
        Edit a task's title with proper error handling.
        
        Args:
            task_index (int): Index of task to edit (1-based)
            new_title (str): New title for the task
            
        Returns:
            tuple[bool, str]: (Success status, Message)
        """
        try:
            # Convert to 0-based index
            index = task_index - 1
            
            # Check if index is valid
            if not self.task_list.check_task_index(index):
                return False, "Invalid task number. Please try again."
            
            # Edit task title
            task = self.task_list.get_task(index)
            task.change_title(new_title)
            
            return True, f"Task title updated to '{new_title}'."
            
        except Exception as e:
            return False, f"Error editing task title: {e}"
    
    def edit_task_date(self, task_index: int, new_date: datetime.datetime) -> tuple[bool, str]:
        """
        Edit a task's due date with proper error handling.
        
        Args:
            task_index (int): Index of task to edit (1-based)
            new_date (datetime.datetime): New due date for the task
            
        Returns:
            tuple[bool, str]: (Success status, Message)
        """
        try:
            # Convert to 0-based index
            index = task_index - 1
            
            # Check if index is valid
            if not self.task_list.check_task_index(index):
                return False, "Invalid task number. Please try again."
            
            # Edit task date
            task = self.task_list.get_task(index)
            task.change_date(new_date)
            
            return True, f"Task due date updated to {new_date.strftime('%Y-%m-%d')}."
            
        except Exception as e:
            return False, f"Error editing task date: {e}"
    
    def load_tasks_from_dao(self, file_path: str, dao_type: str) -> tuple[bool, str]:
        """
        Load tasks from DAO with proper error handling.
        
        Args:
            file_path (str): Path to the data file
            dao_type (str): Type of DAO ('test', 'csv', 'pickle')
            
        Returns:
            tuple[bool, str]: (Success status, Message)
        """
        try:
            # Create appropriate DAO instance
            if dao_type.lower() == 'test':
                self.dao = TaskTestDAO(file_path)
            elif dao_type.lower() == 'pickle':
                self.dao = TaskPickleDAO(file_path)
            else:  # Default to CSV
                self.dao = TaskCsvDAO(file_path)
            
            # Load tasks
            loaded_tasks = self.dao.get_all_tasks()
            
            # Add loaded tasks to task list
            for task in loaded_tasks:
                self.task_list.add_task(task)
            
            return True, f"Successfully loaded {len(loaded_tasks)} tasks using {dao_type.upper()} DAO."
            
        except Exception as e:
            return False, f"Error loading tasks: {e}"
    
    def save_tasks_to_dao(self, file_path: str = None, dao_type: str = None) -> tuple[bool, str]:
        """
        Save tasks to DAO with proper error handling.
        
        Args:
            file_path (str): Path to save data (optional if DAO already set)
            dao_type (str): Type of DAO (optional if DAO already set)
            
        Returns:
            tuple[bool, str]: (Success status, Message)
        """
        try:
            # Create DAO if not already set
            if self.dao is None and file_path and dao_type:
                if dao_type.lower() == 'test':
                    self.dao = TaskTestDAO(file_path)
                elif dao_type.lower() == 'pickle':
                    self.dao = TaskPickleDAO(file_path)
                else:  # Default to CSV
                    self.dao = TaskCsvDAO(file_path)
            
            if self.dao is None:
                return False, "No DAO configured for saving. Please load tasks first or specify DAO type."
            
            # Save tasks
            self.dao.save_all_tasks(self.task_list.tasks)
            return True, "Tasks saved successfully."
            
        except Exception as e:
            return False, f"Error saving tasks: {e}"
    
    def get_task_count(self) -> dict[str, int]:
        """
        Get task count statistics.
        
        Returns:
            dict[str, int]: Dictionary with task count statistics
        """
        total_tasks = len(self.task_list.tasks)
        uncompleted_tasks = len(self.task_list.uncompleted_tasks)
        completed_tasks = total_tasks - uncompleted_tasks
        overdue_tasks = len(self.get_overdue_tasks())
        
        return {
            "total": total_tasks,
            "uncompleted": uncompleted_tasks,
            "completed": completed_tasks,
            "overdue": overdue_tasks
        }
