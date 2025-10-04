"""
Task Factory Module - Week 7 SOLID Principles and Factory Pattern

Demonstrates Factory design pattern implementation:
- Open/Closed Principle (open for extension, closed for modification)
- Single Responsibility Principle (only responsible for task creation)
- Centralized object creation logic
- Easy extension for new task types

Author: [GLORY TITILOPE OLANREWAJU]
"""

import datetime
from typing import Any
from task import Task, RecurringTask


class TaskFactory:
    """Factory class implementing Factory design pattern for task creation."""

    @staticmethod
    def create_task(title: str, date: datetime.datetime, **kwargs: Any) -> Task:
        """
        Create Task or RecurringTask based on parameters - demonstrates Factory pattern.

        Args:
            title (str): Task title
            date (datetime.datetime): Due date
            **kwargs: Additional parameters (interval for RecurringTask)

        Returns:
            Task: Task or RecurringTask instance
        """
        if "interval" in kwargs:
            interval = kwargs["interval"]
            return RecurringTask(title, date, interval)
        else:
            return Task(title, date)
    
    @staticmethod
    def create_task_with_description(title: str, date: datetime.datetime, 
                                   description: str = "", **kwargs: Any) -> Task:
        """
        Create a Task with description support (portfolio extension).
        
        This method extends the factory to support task descriptions,
        demonstrating how the Factory pattern can be extended without
        modifying existing code (Open/Closed Principle).
        
        Args:
            title (str): The title of the task
            date (datetime.datetime): The due date of the task
            description (str): The task description
            **kwargs (Any): Additional parameters for task creation
            
        Returns:
            Task: Task instance with description set
        """
        # Create task using main factory method
        task = TaskFactory.create_task(title, date, **kwargs)
        
        # Set description if the task supports it
        if hasattr(task, 'description'):
            task.description = description
            
        return task
    
    @staticmethod
    def get_supported_task_types() -> list[str]:
        """
        Get list of supported task types.
        
        This method provides information about available task types,
        useful for UI components and validation.
        
        Returns:
            list[str]: List of supported task type names
        """
        return ["Task", "RecurringTask"]
    
    @staticmethod
    def is_recurring_task_params(kwargs: dict[str, Any]) -> bool:
        """
        Check if parameters indicate a recurring task should be created.
        
        This helper method encapsulates the logic for determining task type,
        making it easier to extend or modify the criteria in the future.
        
        Args:
            kwargs (dict[str, Any]): Parameters to check
            
        Returns:
            bool: True if parameters indicate recurring task, False otherwise
        """
        return "interval" in kwargs and kwargs["interval"] is not None
