"""
Task Manager Controller Module - Portfolio Quality Implementation

This module implements the Controller pattern for managing business logic
with comprehensive support for all task types including PriorityTask.

The Controller provides:
- Centralized business logic management
- Separation of concerns between UI and business logic
- Exception handling for business operations
- Coordination between different components
- Support for Task, RecurringTask, and PriorityTask

Classes:
- TaskManagerController: Enhanced controller for task management operations

Author: [Moses Gana]
Date: 2024
Version: 8.0 (Portfolio Quality with PriorityTask Support)
"""


# IMPORTS


import datetime  # For date/time operations
from typing import Optional, Any, List, Tuple  # For type hints
from tasklist import TaskList  # Import TaskList class
from task import AbstractTask, Task, RecurringTask, PriorityTask  # Import Task classes
from task_factory import TaskFactory  # Import Factory for task creation
from abstract_dao import AbstractDAO, TaskTestDAO, TaskCsvDAO  # Import DAO classes


# TASK MANAGER CONTROLLER CLASS DEFINITION


class TaskManagerController:
    """
    Enhanced controller class for managing task operations and business logic.
    
    This class demonstrates:
    - Single Responsibility Principle (only handles business logic)
    - Dependency Inversion Principle (depends on abstractions, not concrete classes)
    - Separation of concerns (business logic separated from UI)
    - Exception handling for business operations
    - Support for all task types including PriorityTask
    
    The controller coordinates between TaskList, DAO classes, and TaskFactory
    while providing a clean interface for the UI layer.
    """
    
    def __init__(self, owner: str) -> None:
        """
        Initialize the controller with a task list owner.
        
        Args:
            owner (str): Name of the task list owner
        """
        self.task_list = TaskList(owner)
        self.dao: Optional[AbstractDAO] = None  # Will be set when loading/saving
    
    def create_regular_task(self, title: str, due_date: datetime.datetime, description: str = "") -> bool:
        """
        Create a new regular task using the TaskFactory.
        
        Args:
            title (str): Task title
            due_date (datetime.datetime): Task due date
            description (str): Optional task description
            
        Returns:
            bool: True if task created successfully, False otherwise
        """
        try:
            task = TaskFactory.create_task(title, due_date, description=description)
            self.task_list.add_task(task)
            return True
        except Exception as e:
            print(f"Error creating regular task: {e}")
            return False
    
    def create_recurring_task(self, title: str, due_date: datetime.datetime, 
                            interval_days: int, description: str = "") -> bool:
        """
        Create a new recurring task using the TaskFactory.
        
        Args:
            title (str): Task title
            due_date (datetime.datetime): Task due date
            interval_days (int): Interval in days for recurring tasks
            description (str): Optional task description
            
        Returns:
            bool: True if task created successfully, False otherwise
        """
        try:
            interval = datetime.timedelta(days=interval_days)
            task = TaskFactory.create_task(title, due_date, interval=interval, description=description)
            self.task_list.add_task(task)
            return True
        except Exception as e:
            print(f"Error creating recurring task: {e}")
            return False
    
    def create_priority_task(self, title: str, due_date: datetime.datetime, 
                           priority_level: int, description: str = "") -> bool:
        """
        Create a new priority task using the TaskFactory.
        
        Args:
            title (str): Task title
            due_date (datetime.datetime): Task due date
            priority_level (int): Priority level (1=low, 2=medium, 3=high)
            description (str): Optional task description
            
        Returns:
            bool: True if task created successfully, False otherwise
        """
        try:
            task = TaskFactory.create_task(title, due_date, priority_level=priority_level, description=description)
            self.task_list.add_task(task)
            return True
        except Exception as e:
            print(f"Error creating priority task: {e}")
            return False
    
    def get_uncompleted_tasks(self) -> List[AbstractTask]:
        """
        Get all uncompleted tasks using the property.
        
        Returns:
            List[AbstractTask]: List of uncompleted tasks
        """
        return self.task_list.uncompleted_tasks
    
    def get_all_tasks(self) -> List[AbstractTask]:
        """
        Get all tasks in the task list.
        
        Returns:
            List[AbstractTask]: List of all tasks
        """
        return self.task_list.tasks
    
    def get_overdue_tasks(self) -> List[AbstractTask]:
        """
        Get all overdue tasks.
        
        Returns:
            List[AbstractTask]: List of overdue tasks
        """
        overdue_tasks = []
        current_time = datetime.datetime.now()
        
        for task in self.task_list.tasks:
            if task.date_due < current_time and not task.completed:
                overdue_tasks.append(task)
        
        return overdue_tasks
    
    def get_priority_tasks(self) -> List[PriorityTask]:
        """
        Get all priority tasks sorted by priority level (high to low).
        
        Returns:
            List[PriorityTask]: List of priority tasks sorted by priority
        """
        priority_tasks = [task for task in self.task_list.tasks if isinstance(task, PriorityTask)]
        # Sort by priority level (3=high, 2=medium, 1=low) - descending order
        priority_tasks.sort(key=lambda task: task.priority_level, reverse=True)
        return priority_tasks
    
    def get_task_by_number(self, task_number: int) -> Optional[AbstractTask]:
        """
        Get a task by its display number (1-based).
        
        Args:
            task_number (int): Task number (1-based)
            
        Returns:
            Optional[AbstractTask]: Task if found, None otherwise
        """
        try:
            index = task_number - 1
            if self.task_list.check_task_index(index):
                return self.task_list.get_task(index)
            return None
        except Exception:
            return None
    
    def mark_task_completed(self, task_index: int) -> Tuple[bool, str]:
        """
        Mark a task as completed with proper error handling.
        
        Args:
            task_index (int): Index of task to mark as completed (1-based)
            
        Returns:
            Tuple[bool, str]: (Success status, Message)
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
            
            task_type = task.get_task_type()
            if isinstance(task, PriorityTask):
                priority_str = task.get_priority_string()
                return True, f"{priority_str.capitalize()} priority task '{task.title}' marked as completed."
            elif isinstance(task, RecurringTask):
                return True, f"Recurring task '{task.title}' completed. Next due: {task.date_due.strftime('%Y-%m-%d')}"
            else:
                return True, f"Task '{task.title}' marked as completed."
            
        except Exception as e:
            return False, f"Error marking task as completed: {e}"
    
    def remove_task(self, task_index: int) -> Tuple[bool, str]:
        """
        Remove a task with proper error handling.
        
        Args:
            task_index (int): Index of task to remove (1-based)
            
        Returns:
            Tuple[bool, str]: (Success status, Message)
        """
        try:
            # Convert to 0-based index
            index = task_index - 1
            
            # Check if index is valid
            if not self.task_list.check_task_index(index):
                return False, "Invalid task number. Please try again."
            
            # Get task info before removal
            task = self.task_list.get_task(index)
            task_title = task.title
            task_type = task.get_task_type()
            
            # Remove task
            self.task_list.remove_task(index)
            return True, f"{task_type} '{task_title}' removed successfully."
            
        except Exception as e:
            return False, f"Error removing task: {e}"
    
    def edit_task_title(self, task_index: int, new_title: str) -> Tuple[bool, str]:
        """
        Edit a task's title with proper error handling.
        
        Args:
            task_index (int): Index of task to edit (1-based)
            new_title (str): New title for the task
            
        Returns:
            Tuple[bool, str]: (Success status, Message)
        """
        try:
            # Convert to 0-based index
            index = task_index - 1
            
            # Check if index is valid
            if not self.task_list.check_task_index(index):
                return False, "Invalid task number. Please try again."
            
            # Edit task title
            task = self.task_list.get_task(index)
            old_title = task.title
            task.change_title(new_title)
            
            return True, f"Task title updated from '{old_title}' to '{new_title}'."
            
        except Exception as e:
            return False, f"Error editing task title: {e}"
    
    def edit_task_date(self, task_index: int, new_date: datetime.datetime) -> Tuple[bool, str]:
        """
        Edit a task's due date with proper error handling.
        
        Args:
            task_index (int): Index of task to edit (1-based)
            new_date (datetime.datetime): New due date for the task
            
        Returns:
            Tuple[bool, str]: (Success status, Message)
        """
        try:
            # Convert to 0-based index
            index = task_index - 1
            
            # Check if index is valid
            if not self.task_list.check_task_index(index):
                return False, "Invalid task number. Please try again."
            
            # Edit task date
            task = self.task_list.get_task(index)
            old_date = task.date_due
            task.change_date(new_date)
            
            return True, f"Task due date updated from {old_date.strftime('%Y-%m-%d')} to {new_date.strftime('%Y-%m-%d')}."
            
        except Exception as e:
            return False, f"Error editing task date: {e}"
    
    def edit_task_description(self, task_index: int, new_description: str) -> Tuple[bool, str]:
        """
        Edit a task's description with proper error handling.
        
        Args:
            task_index (int): Index of task to edit (1-based)
            new_description (str): New description for the task
            
        Returns:
            Tuple[bool, str]: (Success status, Message)
        """
        try:
            # Convert to 0-based index
            index = task_index - 1
            
            # Check if index is valid
            if not self.task_list.check_task_index(index):
                return False, "Invalid task number. Please try again."
            
            # Edit task description
            task = self.task_list.get_task(index)
            old_description = task.description
            task.change_description(new_description)
            
            return True, f"Task description updated."
            
        except Exception as e:
            return False, f"Error editing task description: {e}"
    
    def edit_task_priority(self, task_index: int, new_priority: int) -> Tuple[bool, str]:
        """
        Edit a priority task's priority level with proper error handling.
        
        Args:
            task_index (int): Index of task to edit (1-based)
            new_priority (int): New priority level (1-3)
            
        Returns:
            Tuple[bool, str]: (Success status, Message)
        """
        try:
            # Convert to 0-based index
            index = task_index - 1
            
            # Check if index is valid
            if not self.task_list.check_task_index(index):
                return False, "Invalid task number. Please try again."
            
            # Get task and check if it's a priority task
            task = self.task_list.get_task(index)
            if not isinstance(task, PriorityTask):
                return False, "Selected task is not a priority task."
            
            # Edit priority level
            old_priority = task.get_priority_string()
            task.priority_level = new_priority
            new_priority_str = task.get_priority_string()
            
            return True, f"Task priority updated from {old_priority} to {new_priority_str}."
            
        except Exception as e:
            return False, f"Error editing task priority: {e}"

    def load_tasks_from_dao(self, file_path: str, dao_type: str) -> Tuple[bool, str]:
        """
        Load tasks from DAO with proper error handling.

        Args:
            file_path (str): Path to the data file
            dao_type (str): Type of DAO ('test', 'csv')

        Returns:
            Tuple[bool, str]: (Success status, Message)
        """
        try:
            # Create appropriate DAO instance
            if dao_type.lower() == 'test':
                self.dao = TaskTestDAO(file_path)
            else:  # Default to CSV
                self.dao = TaskCsvDAO(file_path)

            # Load tasks
            loaded_tasks = self.dao.get_all_tasks()

            # Add loaded tasks to task list
            for task in loaded_tasks:
                self.task_list.add_task(task)

            # Count task types
            regular_count = sum(1 for task in loaded_tasks if task.get_task_type() == "Task")
            recurring_count = sum(1 for task in loaded_tasks if task.get_task_type() == "RecurringTask")
            priority_count = sum(1 for task in loaded_tasks if task.get_task_type() == "PriorityTask")

            return True, (f"Successfully loaded {len(loaded_tasks)} tasks using {dao_type.upper()} DAO. "
                         f"({regular_count} regular, {recurring_count} recurring, {priority_count} priority)")

        except Exception as e:
            return False, f"Error loading tasks: {e}"

    def save_tasks_to_dao(self, file_path: str = None, dao_type: str = None) -> Tuple[bool, str]:
        """
        Save tasks to DAO with proper error handling.

        Args:
            file_path (str): Path to save data (optional if DAO already set)
            dao_type (str): Type of DAO (optional if DAO already set)

        Returns:
            Tuple[bool, str]: (Success status, Message)
        """
        try:
            # Create DAO if not already set
            if self.dao is None and file_path and dao_type:
                if dao_type.lower() == 'test':
                    self.dao = TaskTestDAO(file_path)
                else:  # Default to CSV
                    self.dao = TaskCsvDAO(file_path)

            if self.dao is None:
                return False, "No DAO configured for saving. Please load tasks first or specify DAO type."

            # Save tasks
            self.dao.save_all_tasks(self.task_list.tasks)

            # Count task types
            regular_count = sum(1 for task in self.task_list.tasks if task.get_task_type() == "Task")
            recurring_count = sum(1 for task in self.task_list.tasks if task.get_task_type() == "RecurringTask")
            priority_count = sum(1 for task in self.task_list.tasks if task.get_task_type() == "PriorityTask")

            return True, (f"Tasks saved successfully. "
                         f"({regular_count} regular, {recurring_count} recurring, {priority_count} priority)")

        except Exception as e:
            return False, f"Error saving tasks: {e}"

    def get_task_count(self) -> dict[str, int]:
        """
        Get comprehensive task count statistics.

        Returns:
            dict[str, int]: Dictionary with task count statistics
        """
        total_tasks = len(self.task_list.tasks)
        uncompleted_tasks = len(self.task_list.uncompleted_tasks)
        completed_tasks = total_tasks - uncompleted_tasks
        overdue_tasks = len(self.get_overdue_tasks())

        # Count by task type
        regular_tasks = sum(1 for task in self.task_list.tasks if task.get_task_type() == "Task")
        recurring_tasks = sum(1 for task in self.task_list.tasks if task.get_task_type() == "RecurringTask")
        priority_tasks = sum(1 for task in self.task_list.tasks if task.get_task_type() == "PriorityTask")

        # Count priority levels
        high_priority = sum(1 for task in self.task_list.tasks
                           if isinstance(task, PriorityTask) and task.priority_level == 3)
        medium_priority = sum(1 for task in self.task_list.tasks
                             if isinstance(task, PriorityTask) and task.priority_level == 2)
        low_priority = sum(1 for task in self.task_list.tasks
                          if isinstance(task, PriorityTask) and task.priority_level == 1)

        return {
            "total": total_tasks,
            "uncompleted": uncompleted_tasks,
            "completed": completed_tasks,
            "overdue": overdue_tasks,
            "regular": regular_tasks,
            "recurring": recurring_tasks,
            "priority": priority_tasks,
            "high_priority": high_priority,
            "medium_priority": medium_priority,
            "low_priority": low_priority
        }
