"""
Abstract Classes in ToDo Application - Week 8

Demonstrates abstract classes with @abstractmethod decorator:
- AbstractTask: Base class for all task types
- AbstractDAO: Base class for all data access objects
- Polymorphism through consistent interfaces
- Interface segregation principle from SOLID

Author: [MOSES GANA]
"""

from abc import ABC, abstractmethod
import datetime
from typing import List, Optional, Any


# ABSTRACT TASK CLASS

class AbstractTask(ABC):
    """Abstract base class for all task types with @abstractmethod decorator."""

    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        """Initialize abstract task with common attributes."""
        self.title = title
        self.date_due = date_due
        self.completed = False
        self.date_created = datetime.datetime.now()

    @abstractmethod
    def mark_as_completed(self) -> None:
        """Abstract method - must be implemented by subclasses."""
        pass

    @abstractmethod
    def get_task_type(self) -> str:
        """Abstract method to get task type identifier."""
        pass
    
    def change_title(self, new_title: str) -> None:
        """Change task title - common implementation."""
        self.title = new_title

    def change_date(self, new_date: datetime.datetime) -> None:
        """Change due date - common implementation."""
        self.date_due = new_date

    def is_overdue(self) -> bool:
        """Check if task is overdue - common implementation."""
        return datetime.datetime.now() > self.date_due and not self.completed

    def __str__(self) -> str:
        """String representation - common implementation."""
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.title} [{status}] Created: {self.date_created} Due: {self.date_due}"


class Task(AbstractTask):
    """
    Concrete implementation of a regular task.
    
    This class provides specific implementation for regular tasks
    that don't have recurring behavior.
    """
    
    def mark_as_completed(self) -> None:
        """Mark regular task as completed."""
        self.completed = True
    
    def get_task_type(self) -> str:
        """Get task type identifier."""
        return "Task"


class RecurringTask(AbstractTask):
    """
    Concrete implementation of a recurring task.
    
    This class extends the abstract task with recurring-specific behavior,
    including interval management and due date updates upon completion.
    """
    
    def __init__(self, title: str, date_due: datetime.datetime, 
                 interval: datetime.timedelta) -> None:
        """
        Initialize recurring task with interval.
        
        Args:
            title: Task title
            date_due: Initial due date
            interval: Recurrence interval
        """
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: List[datetime.datetime] = []
    
    def mark_as_completed(self) -> None:
        """
        Mark recurring task as completed and update due date.
        
        This demonstrates polymorphism - same method name as Task
        but different behavior for recurring tasks.
        """
        self.completed_dates.append(datetime.datetime.now())
        self.date_due += self.interval  # Update to next occurrence
        # Note: recurring tasks don't stay "completed"
    
    def get_task_type(self) -> str:
        """Get task type identifier."""
        return "RecurringTask"
    
    def __str__(self) -> str:
        """Enhanced string representation for recurring tasks."""
        return (f"{self.title} - Recurring (created: {self.date_created}, "
                f"due: {self.date_due}, completed {len(self.completed_dates)} times, "
                f"interval: {self.interval})")


# ABSTRACT DAO CLASS

class AbstractDAO(ABC):
    """
    Abstract base class for all Data Access Objects.
    
    This class defines the common interface that all DAO implementations
    must follow, ensuring consistent data access patterns across different
    storage mechanisms (CSV, database, pickle, etc.).
    """
    
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


class TaskTestDAO(AbstractDAO):
    """
    Test DAO implementation for development and testing.
    
    This class provides a concrete implementation of the abstract DAO
    that returns predefined test data instead of reading from files.
    """
    
    def get_all_tasks(self) -> List[AbstractTask]:
        """
        Get predefined test tasks.
        
        Returns:
            List[AbstractTask]: List of test tasks
        """
        # Create test tasks using the abstract task interface
        tasks = [
            Task("Buy groceries", datetime.datetime.now() + datetime.timedelta(days=1)),
            Task("Complete assignment", datetime.datetime.now() + datetime.timedelta(days=3)),
            RecurringTask("Weekly meeting", datetime.datetime.now() + datetime.timedelta(days=2),
                         datetime.timedelta(days=7))
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
            print(f"  {i}. {task.title} - {status}")


class TaskMemoryDAO(AbstractDAO):
    """
    In-memory DAO implementation for temporary storage.
    
    This class demonstrates another concrete implementation of the abstract DAO
    that stores tasks in memory (useful for testing or temporary operations).
    """
    
    def __init__(self, storage_path: str = "memory") -> None:
        """Initialize memory DAO with in-memory storage."""
        super().__init__(storage_path)
        self._memory_storage: List[AbstractTask] = []
    
    def get_all_tasks(self) -> List[AbstractTask]:
        """
        Get all tasks from memory storage.
        
        Returns:
            List[AbstractTask]: List of tasks in memory
        """
        print(f"Retrieved {len(self._memory_storage)} tasks from memory")
        return self._memory_storage.copy()  # Return copy to prevent external modification
    
    def save_all_tasks(self, tasks: List[AbstractTask]) -> None:
        """
        Save all tasks to memory storage.
        
        Args:
            tasks: List of tasks to save in memory
        """
        self._memory_storage = tasks.copy()  # Store copy to prevent external modification
        print(f"Saved {len(tasks)} tasks to memory storage")


# DEMONSTRATION FUNCTIONS

def demonstrate_abstract_task_polymorphism() -> None:
    """Demonstrate polymorphism with abstract task classes."""
    print("=== Abstract Task Polymorphism ===")
    
    # Create different task types using the same interface
    tasks: List[AbstractTask] = [
        Task("Regular task", datetime.datetime.now() + datetime.timedelta(days=1)),
        RecurringTask("Recurring task", datetime.datetime.now() + datetime.timedelta(days=2),
                     datetime.timedelta(days=7))
    ]
    
    # Demonstrate polymorphism - same method calls, different behaviors
    for task in tasks:
        print(f"Task type: {task.get_task_type()}")
        print(f"Before completion: {task}")
        task.mark_as_completed()
        print(f"After completion: {task}")
        print(f"Is overdue: {task.is_overdue()}")
        print("-" * 50)

def demonstrate_abstract_dao_polymorphism() -> None:
    """Demonstrate polymorphism with abstract DAO classes."""
    print("=== Abstract DAO Polymorphism ===")
    
    # Create different DAO types using the same interface
    daos: List[AbstractDAO] = [
        TaskTestDAO("test_storage.txt"),
        TaskMemoryDAO()
    ]
    
    # Demonstrate polymorphism - same method calls, different implementations
    for dao in daos:
        print(f"DAO Info: {dao.get_storage_info()}")
        
        # Load tasks
        tasks = dao.get_all_tasks()
        
        # Modify a task to show state change
        if tasks:
            tasks[0].mark_as_completed()
        
        # Save tasks back
        dao.save_all_tasks(tasks)
        print("-" * 50)

def main() -> None:
    """
    Main function to demonstrate abstract classes in ToDo application.
    """
    print("Week 8 Optional Extra Task - Abstract Classes in ToDo Application")
    # Demonstrate abstract task enforcement
    print("\n1. ABSTRACT CLASS ENFORCEMENT")
    try:
        # This should raise TypeError
        abstract_task = AbstractTask("Test", datetime.datetime.now())
        print("ERROR: Abstract task was instantiated!")
    except TypeError as e:
        print(f"Abstract task correctly prevented instantiation: {e}")
    
    try:
        # This should raise TypeError
        abstract_dao = AbstractDAO("test_path")
        print("ERROR: Abstract DAO was instantiated!")
    except TypeError as e:
        print(f"Abstract DAO correctly prevented instantiation: {e}")

if __name__ == "__main__":
    main()
