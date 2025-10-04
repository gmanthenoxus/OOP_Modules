"""
User Interface Module - Portfolio Quality Implementation

This module implements the presentation layer following SOLID principles
with comprehensive support for all task types including PriorityTask.

The UI layer provides:
- User input/output handling for all task types
- Menu presentation and navigation
- Priority task creation and management
- Enhanced error message display
- Separation from business logic
- Support for Task, RecurringTask, and PriorityTask

Classes:
- CommandLineUI: Enhanced command-line interface for the ToDo application

Author: [Moses Gana]
Date: 2024
Version: 8.0 (Portfolio Quality with PriorityTask Support)
"""


# IMPORTS


import datetime  # For date parsing
from typing import Optional, Dict, Any
from task_manager_controller import TaskManagerController  # Import controller
from task import PriorityTask  # Import for priority level validation


# COMMAND LINE UI CLASS DEFINITION


class CommandLineUI:
    """
    Enhanced command-line user interface for the ToDo application.
    
    This class demonstrates:
    - Single Responsibility Principle (only handles UI concerns)
    - Separation of concerns (UI separated from business logic)
    - Dependency Inversion Principle (depends on controller abstraction)
    - Support for all task types including PriorityTask
    
    The UI class handles all user interaction while delegating business
    logic to the TaskManagerController.
    """
    
    def __init__(self) -> None:
        """Initialize the UI with a controller instance."""
        self.controller: Optional[TaskManagerController] = None
    
    def run(self) -> None:
        """
        Main application loop with comprehensive task type support.
        
        This method handles the overall application flow while delegating
        specific operations to the controller.
        """
        # Initialize application
        self._initialize_application()
        
        # Main application loop
        while True:
            try:
                self._print_menu()
                choice = input("Enter your choice: ").strip()
                
                if choice == "1":
                    self._handle_add_task()
                elif choice == "2":
                    self._handle_view_tasks()
                elif choice == "3":
                    self._handle_view_overdue_tasks()
                elif choice == "4":
                    self._handle_view_priority_tasks()
                elif choice == "5":
                    self._handle_remove_task()
                elif choice == "6":
                    self._handle_mark_completed()
                elif choice == "7":
                    self._handle_edit_task()
                elif choice == "8":
                    self._handle_load_tasks()
                elif choice == "9":
                    self._handle_save_tasks()
                elif choice == "10":
                    self._handle_quit()
                    break
                else:
                    print("Invalid choice. Please try again.")
                    
            except KeyboardInterrupt:
                print("\n\nApplication interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                print("Please try again.")
    
    def _initialize_application(self) -> None:
        """Initialize the application with user input."""
        print("=== Enhanced ToDo Application - Portfolio Quality ===")
        print("Supporting Task, RecurringTask, and PriorityTask types")
        owner_name = input("Enter the name of the task list owner: ").strip()
        
        if not owner_name:
            owner_name = "Default User"
            
        self.controller = TaskManagerController(owner_name)
        print(f"Welcome, {owner_name}!")
        
        # Display task statistics
        stats = self.controller.get_task_count()
        print(f"Current tasks: {stats['total']} total, {stats['uncompleted']} uncompleted")
    
    def _print_menu(self) -> None:
        """Display the enhanced main menu with priority task support."""
        print("\n" + "="*60)
        print("Enhanced ToDo List Manager - Portfolio Implementation")
        print("="*60)
        print("1. Add a task (Regular/Recurring/Priority)")
        print("2. View tasks (uncompleted only)")
        print("3. View overdue tasks")
        print("4. View tasks by priority")
        print("5. Remove a task")
        print("6. Mark task as completed")
        print("7. Edit task")
        print("8. Load tasks from DAO")
        print("9. Save tasks to DAO")
        print("10. Quit")
        print("="*60)
    
    def _handle_add_task(self) -> None:
        """Handle adding a new task with support for all task types."""
        try:
            print("\n--- Add New Task ---")
            
            # Get task type
            print("Task types:")
            print("1. Regular Task")
            print("2. Recurring Task")
            print("3. Priority Task")
            
            task_type_choice = input("Select task type (1-3): ").strip()
            
            # Get common task information
            title = input("Enter the task title: ").strip()
            if not title:
                print("Task title cannot be empty.")
                return
            
            # Get due date
            date_input = input("Enter due date (YYYY-MM-DD): ").strip()
            try:
                due_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return
            
            # Get description
            description = input("Enter task description (optional): ").strip()
            
            # Handle different task types
            if task_type_choice == "1":
                # Regular task
                success = self.controller.create_regular_task(title, due_date, description)
                
            elif task_type_choice == "2":
                # Recurring task
                try:
                    interval_input = input("Enter interval in days [default: 7]: ").strip()
                    interval_days = int(interval_input) if interval_input else 7
                except ValueError:
                    print("Invalid interval. Using default of 7 days.")
                    interval_days = 7
                
                success = self.controller.create_recurring_task(title, due_date, interval_days, description)
                
            elif task_type_choice == "3":
                # Priority task
                self._display_priority_levels()
                try:
                    priority_input = input("Enter priority level (1-3): ").strip()
                    priority_level = int(priority_input)
                    
                    if priority_level not in [1, 2, 3]:
                        print("Priority level must be 1, 2, or 3.")
                        return
                        
                except ValueError:
                    print("Invalid priority level. Please enter 1, 2, or 3.")
                    return
                
                success = self.controller.create_priority_task(title, due_date, priority_level, description)
                
            else:
                print("Invalid task type selection.")
                return
            
            if success:
                print("✓ Task added successfully!")
            else:
                print("✗ Failed to create task.")
                
        except Exception as e:
            print(f"Error adding task: {e}")
    
    def _display_priority_levels(self) -> None:
        """Display available priority levels."""
        print("\nPriority levels:")
        priority_mapping = PriorityTask.get_priority_descriptions()
        for level, description in priority_mapping.items():
            print(f"{level}. {description.capitalize()}")
    
    def _handle_view_tasks(self) -> None:
        """Handle viewing uncompleted tasks with enhanced display."""
        try:
            tasks = self.controller.get_uncompleted_tasks()
            
            if not tasks:
                print("No uncompleted tasks found.")
                return
            
            print("\n📋 Uncompleted Tasks:")
            print("-" * 80)
            
            all_tasks = self.controller.get_all_tasks()
            for task in tasks:
                # Get original index for display
                original_index = all_tasks.index(task) + 1
                task_type = task.get_task_type()
                
                # Enhanced display with task type and priority info
                priority_info = ""
                if hasattr(task, 'get_priority_string'):
                    priority_info = f" [Priority: {task.get_priority_string().upper()}]"
                
                print(f"{original_index:2d}. {task}{priority_info}")
                
        except Exception as e:
            print(f"Error viewing tasks: {e}")
    
    def _handle_view_overdue_tasks(self) -> None:
        """Handle viewing overdue tasks."""
        try:
            overdue_tasks = self.controller.get_overdue_tasks()
            
            if not overdue_tasks:
                print("No overdue tasks found.")
                return
            
            print("\n⚠️  Overdue Tasks:")
            print("-" * 80)
            
            all_tasks = self.controller.get_all_tasks()
            for task in overdue_tasks:
                # Get original index for display
                original_index = all_tasks.index(task) + 1
                days_overdue = (datetime.datetime.now() - task.date_due).days
                
                priority_info = ""
                if hasattr(task, 'get_priority_string'):
                    priority_info = f" [Priority: {task.get_priority_string().upper()}]"
                
                print(f"{original_index:2d}. {task} (Overdue by {days_overdue} days){priority_info}")
                
        except Exception as e:
            print(f"Error viewing overdue tasks: {e}")
    
    def _handle_view_priority_tasks(self) -> None:
        """Handle viewing tasks filtered by priority level."""
        try:
            priority_tasks = self.controller.get_priority_tasks()
            
            if not priority_tasks:
                print("No priority tasks found.")
                return
            
            print("\n🎯 Priority Tasks (sorted by priority):")
            print("-" * 80)
            
            # Group tasks by priority level
            priority_groups = {1: [], 2: [], 3: []}
            all_tasks = self.controller.get_all_tasks()
            
            for task in priority_tasks:
                priority_groups[task.priority_level].append(task)
            
            # Display by priority level (high to low)
            for priority_level in [3, 2, 1]:
                tasks_at_level = priority_groups[priority_level]
                if tasks_at_level:
                    priority_name = PriorityTask.PRIORITY_MAPPING[priority_level].upper()
                    print(f"\n{priority_name} PRIORITY:")
                    
                    for task in tasks_at_level:
                        original_index = all_tasks.index(task) + 1
                        status = "✓" if task.completed else "○"
                        print(f"  {status} {original_index:2d}. {task.title} - Due: {task.date_due.strftime('%Y-%m-%d')}")
                        if task.description:
                            print(f"      Description: {task.description}")
                
        except Exception as e:
            print(f"Error viewing priority tasks: {e}")
    
    def _handle_remove_task(self) -> None:
        """Handle removing a task with proper error handling."""
        try:
            self._handle_view_tasks()  # Show tasks first
            
            if not self.controller.get_all_tasks():
                return
            
            task_num_input = input("Enter the task number to remove: ").strip()
            try:
                task_num = int(task_num_input)
            except ValueError:
                print("Please enter a valid number.")
                return
            
            success, message = self.controller.remove_task(task_num)
            
            if success:
                print(f"✓ {message}")
            else:
                print(f"✗ {message}")
                
        except Exception as e:
            print(f"Error removing task: {e}")
    
    def _handle_mark_completed(self) -> None:
        """Handle marking a task as completed with proper error handling."""
        try:
            self._handle_view_tasks()  # Show uncompleted tasks first
            
            if not self.controller.get_uncompleted_tasks():
                return
            
            task_num_input = input("Enter the task number to mark as completed: ").strip()
            try:
                task_num = int(task_num_input)
            except ValueError:
                print("Please enter a valid number.")
                return
            
            success, message = self.controller.mark_task_completed(task_num)
            
            if success:
                print(f"✓ {message}")
            else:
                print(f"✗ {message}")
                
        except Exception as e:
            print(f"Error marking task as completed: {e}")
    
    def _handle_edit_task(self) -> None:
        """Handle editing a task with support for priority tasks."""
        try:
            self._handle_view_tasks()  # Show tasks first
            
            if not self.controller.get_all_tasks():
                return
            
            task_num_input = input("Enter the task number to edit: ").strip()
            try:
                task_num = int(task_num_input)
            except ValueError:
                print("Please enter a valid number.")
                return
            
            # Get the task to determine available edit options
            task = self.controller.get_task_by_number(task_num)
            if not task:
                print("Invalid task number.")
                return
            
            print(f"\nEditing: {task.title}")
            print("Edit options:")
            print("1. Title")
            print("2. Due date")
            print("3. Description")
            
            if hasattr(task, 'priority_level'):
                print("4. Priority level")
            
            edit_choice = input("Select what to edit (1-4): ").strip()
            
            if edit_choice == "1":
                new_title = input("Enter new title: ").strip()
                if not new_title:
                    print("Title cannot be empty.")
                    return
                success, message = self.controller.edit_task_title(task_num, new_title)
                
            elif edit_choice == "2":
                new_date_input = input("Enter new due date (YYYY-MM-DD): ").strip()
                try:
                    new_date = datetime.datetime.strptime(new_date_input, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    return
                success, message = self.controller.edit_task_date(task_num, new_date)
                
            elif edit_choice == "3":
                new_description = input("Enter new description: ").strip()
                success, message = self.controller.edit_task_description(task_num, new_description)
                
            elif edit_choice == "4" and hasattr(task, 'priority_level'):
                self._display_priority_levels()
                try:
                    new_priority = int(input("Enter new priority level (1-3): ").strip())
                    if new_priority not in [1, 2, 3]:
                        print("Priority level must be 1, 2, or 3.")
                        return
                except ValueError:
                    print("Invalid priority level.")
                    return
                success, message = self.controller.edit_task_priority(task_num, new_priority)
                
            else:
                print("Invalid choice.")
                return
            
            if success:
                print(f"✓ {message}")
            else:
                print(f"✗ {message}")
                
        except Exception as e:
            print(f"Error editing task: {e}")
    
    def _handle_load_tasks(self) -> None:
        """Handle loading tasks from DAO."""
        try:
            file_path = input("Enter file path for loading tasks: ").strip()
            if not file_path:
                print("File path cannot be empty.")
                return
            
            dao_type = input("Use (t)est DAO or (c)sv DAO? [default: csv]: ").strip().lower()
            if dao_type not in ['t', 'test', 'c', 'csv']:
                dao_type = 'csv'
            
            # Map input to full type name
            type_mapping = {'t': 'test', 'c': 'csv'}
            dao_type = type_mapping.get(dao_type, dao_type)
            
            success, message = self.controller.load_tasks_from_dao(file_path, dao_type)
            
            if success:
                print(f"✓ {message}")
                # Show updated statistics
                stats = self.controller.get_task_count()
                print(f"Updated totals: {stats['total']} tasks, {stats['uncompleted']} uncompleted")
            else:
                print(f"✗ {message}")
                
        except Exception as e:
            print(f"Error loading tasks: {e}")
    
    def _handle_save_tasks(self) -> None:
        """Handle saving tasks to DAO."""
        try:
            file_path = input("Enter file path for saving tasks [or press Enter to use existing]: ").strip()
            dao_type = None
            
            if file_path:
                dao_type = input("Use (t)est DAO or (c)sv DAO? [default: csv]: ").strip().lower()
                if dao_type not in ['t', 'test', 'c', 'csv']:
                    dao_type = 'csv'
                
                # Map input to full type name
                type_mapping = {'t': 'test', 'c': 'csv'}
                dao_type = type_mapping.get(dao_type, dao_type)
            
            success, message = self.controller.save_tasks_to_dao(file_path, dao_type)
            
            if success:
                print(f"✓ {message}")
            else:
                print(f"✗ {message}")
                
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def _handle_quit(self) -> None:
        """Handle application quit with optional auto-save."""
        try:
            stats = self.controller.get_task_count()
            
            if stats['total'] > 0:
                save_choice = input("Would you like to save your tasks before quitting? (y/n): ").strip().lower()
                
                if save_choice in ['y', 'yes']:
                    self._handle_save_tasks()
            
            print("Thank you for using Enhanced ToDo Application!")
            print("Portfolio implementation with PriorityTask support complete! 🎯")
            print("Goodbye! 👋")
            
        except Exception as e:
            print(f"Error during quit: {e}")
            print("Goodbye!")


# ADDITIONAL UI HELPER METHODS (if needed for future extensions)

def display_task_statistics(tasks) -> None:
    """
    Display comprehensive task statistics.

    Args:
        tasks: List of tasks to analyze
    """
    if not tasks:
        print("No tasks to analyze.")
        return

    total = len(tasks)
    completed = sum(1 for task in tasks if task.completed)
    overdue = sum(1 for task in tasks if task.is_overdue())

    # Count by type
    regular_tasks = sum(1 for task in tasks if task.get_task_type() == "Task")
    recurring_tasks = sum(1 for task in tasks if task.get_task_type() == "RecurringTask")
    priority_tasks = sum(1 for task in tasks if task.get_task_type() == "PriorityTask")

    print(f"\n📊 Task Statistics:")
    print(f"Total tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Overdue: {overdue}")
    print(f"Regular tasks: {regular_tasks}")
    print(f"Recurring tasks: {recurring_tasks}")
    print(f"Priority tasks: {priority_tasks}")

    # Priority breakdown if there are priority tasks
    if priority_tasks > 0:
        from task import PriorityTask
        high_priority = sum(1 for task in tasks
                           if hasattr(task, 'priority_level') and task.priority_level == 3)
        medium_priority = sum(1 for task in tasks
                             if hasattr(task, 'priority_level') and task.priority_level == 2)
        low_priority = sum(1 for task in tasks
                          if hasattr(task, 'priority_level') and task.priority_level == 1)

        print(f"  - High priority: {high_priority}")
        print(f"  - Medium priority: {medium_priority}")
        print(f"  - Low priority: {low_priority}")
