"""
Users Module - Portfolio Implementation

Demonstrates inheritance and __str__ methods:
- User and Owner classes with inheritance (Week 5)
- Professional string representation methods
- Type hints and comprehensive documentation

Author: [IKENNA FRAKLIN EZEMA]
"""

import datetime


class User:
    """Base User class demonstrating inheritance foundation."""

    def __init__(self, name: str, email: str) -> None:
        """Initialize User with name and email."""
        self.name = name.title()  # Convert to title case for consistency
        self.email = email.lower()  # Convert to lowercase for consistency
        self.date_joined = datetime.datetime.now()  # Auto-generate join timestamp
    
    def __str__(self) -> str:
        """
        Return string representation of the User.
        
        Returns:
            str: Formatted string showing user type and attributes
            
        Example:
            >>> print(user)
            User: John Doe (john@example.com) - Joined: 2024-01-15 10:30:45
        """
        return f"User: {self.name} ({self.email}) - Joined: {self.date_joined.strftime('%Y-%m-%d %H:%M:%S')}"


class Owner(User):
    """
    Owner class representing a user with ownership privileges.
    
    This class demonstrates:
    - Inheritance from User base class
    - Extended functionality for ownership
    - Polymorphic string representation
    - Professional class hierarchy design
    
    Inherits all User attributes and adds:
        permissions (list[str]): List of owner permissions
        tasks_created (int): Number of task lists created by this owner
    """
    
    def __init__(self, name: str, email: str) -> None:
        """
        Initialize a new Owner instance.
        
        Args:
            name (str): The owner's full name
            email (str): The owner's email address
            
        Returns:
            None: Constructors don't return values
            
        Example:
            >>> owner = Owner("moses gana", "b01782775@studentmail.uws.ac.uk")
            >>> print(owner.name)  # Output: "Moses Gana"
        """
        super().__init__(name, email)  # Initialize parent User class
        self.permissions = ["create_tasks", "edit_tasks", "delete_tasks", "manage_users"]  # List of permissions
        self.tasks_created = 0  # Track number of task lists created
    
    def __str__(self) -> str:
        """
        Return string representation of the Owner (polymorphic override).
        
        This method overrides the parent's __str__ method to provide
        Owner-specific information, demonstrating polymorphism.
        
        Returns:
            str: Formatted string showing owner type and attributes
            
        Example:
            >>> print(owner)
            Owner: Moses Gana (b01782775@studentmail.uws.ac.uk) - Joined: 2024-01-15 10:30:45 - Task Lists: 3
        """
        base_info = f"Owner: {self.name} ({self.email})"
        join_info = f"Joined: {self.date_joined.strftime('%Y-%m-%d %H:%M:%S')}"
        task_info = f"Task Lists: {self.tasks_created}"
        return f"{base_info} - {join_info} - {task_info}"
    
    def create_task_list(self) -> None:
        """
        Increment the task list counter when owner creates a new task list.
        
        This method demonstrates owner-specific functionality.
        
        Returns:
            None: Method modifies instance state but doesn't return a value
        """
        self.tasks_created += 1
        print(f"Task list created. Total task lists: {self.tasks_created}")
