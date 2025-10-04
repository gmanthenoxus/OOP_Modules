"""
Task Factory Module - Portfolio Implementation

Demonstrates Factory pattern and Open/Closed Principle:
- Factory design pattern for object creation (Week 7)
- Open/Closed Principle implementation
- Support for Task, RecurringTask, and PriorityTask
- Centralized object creation logic

Author: [IKENNA FRAKLIN EZEMA]
"""

import datetime
from typing import Any, Dict, List, Optional, Union
from task import AbstractTask, Task, RecurringTask, PriorityTask


# TASK FACTORY CLASS DEFINITION


class TaskFactory:
    """
    Factory class for creating Task objects following the Factory design pattern.
    
    This class demonstrates:
    - Factory design pattern implementation
    - Open/Closed Principle (open for extension, closed for modification)
    - Single Responsibility Principle (only responsible for task creation)
    - Centralized object creation logic
    - Support for all task types including PriorityTask
    
    The factory determines the type of task to create based on the parameters
    provided, supporting regular tasks, recurring tasks, and priority tasks.
    """
    
    @staticmethod
    def create_task(title: str, date_due: datetime.datetime, **kwargs: Any) -> AbstractTask:
        """
        Create a Task, RecurringTask, or PriorityTask based on provided parameters.
        
        This static method implements the Factory pattern by creating the
        appropriate task type based on the presence of specific parameters.
        It follows the Open/Closed Principle - new task types can be added
        without modifying this method.
        
        Args:
            title (str): The title of the task
            date_due (datetime.datetime): The due date of the task
            **kwargs (Any): Additional parameters that determine task type:
                - interval (datetime.timedelta): If present, creates RecurringTask
                - priority_level (int): If present, creates PriorityTask
                - description (str): Optional task description for all types
                
        Returns:
            AbstractTask: Task, RecurringTask, or PriorityTask instance based on parameters
            
        Raises:
            ValueError: If invalid priority_level is provided for PriorityTask
            
        Examples:
            >>> # Create a regular task
            >>> normal_task = TaskFactory.create_task(
            ...     "Do homework", 
            ...     datetime.datetime.now() + datetime.timedelta(days=3),
            ...     description="Complete math assignment"
            ... )
            
            >>> # Create a recurring task
            >>> recurring_task = TaskFactory.create_task(
            ...     "Go to the gym", 
            ...     datetime.datetime.now(),
            ...     interval=datetime.timedelta(days=7),
            ...     description="Weekly workout session"
            ... )
            
            >>> # Create a priority task
            >>> priority_task = TaskFactory.create_task(
            ...     "Important meeting",
            ...     datetime.datetime.now() + datetime.timedelta(days=1),
            ...     priority_level=3,
            ...     description="Board meeting preparation"
            ... )
        """
        # Extract common parameters
        description = kwargs.get("description", "")
        
        # Check for priority task first (has priority_level parameter)
        if "priority_level" in kwargs:
            priority_level = kwargs["priority_level"]
            return PriorityTask(title, date_due, priority_level, description)
        
        # Check for recurring task (has interval parameter)
        elif "interval" in kwargs:
            interval = kwargs["interval"]
            return RecurringTask(title, date_due, interval, description)
        
        # Default to regular task
        else:
            return Task(title, date_due, description)
    
    @staticmethod
    def create_task_by_type(task_type: str, title: str, date_due: datetime.datetime, 
                           **kwargs: Any) -> AbstractTask:
        """
        Create a task by explicitly specifying the task type.
        
        This method provides an alternative interface for task creation
        when the task type is known explicitly.
        
        Args:
            task_type (str): Type of task to create ("Task", "RecurringTask", "PriorityTask")
            title (str): The title of the task
            date_due (datetime.datetime): The due date of the task
            **kwargs (Any): Additional parameters specific to task type
            
        Returns:
            AbstractTask: Task instance of the specified type
            
        Raises:
            ValueError: If task_type is not recognized or required parameters are missing
            
        Examples:
            >>> # Create priority task explicitly
            >>> task = TaskFactory.create_task_by_type(
            ...     "PriorityTask", "Urgent task", datetime.datetime.now(), 
            ...     priority_level=3, description="High priority item"
            ... )
        """
        description = kwargs.get("description", "")
        
        if task_type == "Task":
            return Task(title, date_due, description)
        
        elif task_type == "RecurringTask":
            if "interval" not in kwargs:
                raise ValueError("RecurringTask requires 'interval' parameter")
            interval = kwargs["interval"]
            return RecurringTask(title, date_due, interval, description)
        
        elif task_type == "PriorityTask":
            if "priority_level" not in kwargs:
                raise ValueError("PriorityTask requires 'priority_level' parameter")
            priority_level = kwargs["priority_level"]
            return PriorityTask(title, date_due, priority_level, description)
        
        else:
            valid_types = ["Task", "RecurringTask", "PriorityTask"]
            raise ValueError(f"Unknown task type '{task_type}'. Valid types: {valid_types}")
    
    @staticmethod
    def create_priority_task(title: str, date_due: datetime.datetime, 
                           priority_level: int, description: str = "") -> PriorityTask:
        """
        Convenience method to create a PriorityTask with explicit parameters.
        
        Args:
            title (str): The title of the task
            date_due (datetime.datetime): The due date of the task
            priority_level (int): Priority level (1=low, 2=medium, 3=high)
            description (str): Optional task description
            
        Returns:
            PriorityTask: New priority task instance
            
        Raises:
            ValueError: If priority_level is not 1, 2, or 3
        """
        return PriorityTask(title, date_due, priority_level, description)
    
    @staticmethod
    def create_recurring_task(title: str, date_due: datetime.datetime,
                            interval: datetime.timedelta, description: str = "") -> RecurringTask:
        """
        Convenience method to create a RecurringTask with explicit parameters.
        
        Args:
            title (str): The title of the task
            date_due (datetime.datetime): The due date of the task
            interval (datetime.timedelta): Recurrence interval
            description (str): Optional task description
            
        Returns:
            RecurringTask: New recurring task instance
        """
        return RecurringTask(title, date_due, interval, description)
    
    @staticmethod
    def get_supported_task_types() -> List[str]:
        """
        Get list of supported task types.
        
        This method provides information about available task types,
        useful for UI components and validation.
        
        Returns:
            List[str]: List of supported task type names
        """
        return ["Task", "RecurringTask", "PriorityTask"]
    
    @staticmethod
    def get_task_type_info() -> Dict[str, Dict[str, Any]]:
        """
        Get detailed information about each task type and their parameters.
        
        Returns:
            Dict[str, Dict[str, Any]]: Information about each task type
        """
        return {
            "Task": {
                "description": "Basic task with title, due date, and optional description",
                "required_params": ["title", "date_due"],
                "optional_params": ["description"]
            },
            "RecurringTask": {
                "description": "Task that repeats at specified intervals",
                "required_params": ["title", "date_due", "interval"],
                "optional_params": ["description"]
            },
            "PriorityTask": {
                "description": "Task with priority levels (1=low, 2=medium, 3=high)",
                "required_params": ["title", "date_due", "priority_level"],
                "optional_params": ["description"],
                "priority_levels": PriorityTask.get_priority_descriptions()
            }
        }
    
    @staticmethod
    def validate_task_parameters(task_type: str, **kwargs: Any) -> bool:
        """
        Validate parameters for a specific task type.
        
        Args:
            task_type (str): Type of task to validate parameters for
            **kwargs (Any): Parameters to validate
            
        Returns:
            bool: True if parameters are valid, False otherwise
            
        Raises:
            ValueError: If task_type is not recognized
        """
        task_info = TaskFactory.get_task_type_info()
        
        if task_type not in task_info:
            raise ValueError(f"Unknown task type '{task_type}'")
        
        required_params = task_info[task_type]["required_params"]
        
        # Check if all required parameters are present (excluding title and date_due which are always provided)
        for param in required_params:
            if param not in ["title", "date_due"] and param not in kwargs:
                return False
        
        # Validate priority level if it's a PriorityTask
        if task_type == "PriorityTask" and "priority_level" in kwargs:
            priority_level = kwargs["priority_level"]
            valid_levels = PriorityTask.get_valid_priority_levels()
            if priority_level not in valid_levels:
                return False
        
        return True
