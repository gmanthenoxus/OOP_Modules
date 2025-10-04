"""
User Interface Module - Week 7 SOLID Principles

Demonstrates separation of concerns and SOLID principles:
- Single Responsibility Principle (only handles UI concerns)
- Separation of concerns (UI separated from business logic)
- Dependency Inversion Principle (depends on controller abstraction)

Author: [GLORY TITILOPE OLANREWAJU]
"""

import datetime
from task_manager_controller import TaskManagerController


class CommandLineUI:
    """
    Command-line UI demonstrating separation of concerns.

    - Single Responsibility: Only handles UI concerns
    - Separation of concerns: UI separated from business logic
    - Dependency Inversion: Depends on controller abstraction
    """

    def __init__(self) -> None:
        """Initialize UI with controller instance."""
        self.controller: TaskManagerController = None
    
    def run(self) -> None:
        """
        Main application loop with proper separation of concerns.
        
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
                    self._handle_remove_task()
                elif choice == "5":
                    self._handle_mark_completed()
                elif choice == "6":
                    self._handle_edit_task()
                elif choice == "7":
                    self._handle_load_tasks()
                elif choice == "8":
                    self._handle_save_tasks()
                elif choice == "9":
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
        print("=== ToDo Application - Week 7 SOLID Implementation ===")
        owner_name = input("Enter the name of the task list owner: ").strip()
        
        if not owner_name:
            owner_name = "Default User"
            
        self.controller = TaskManagerController(owner_name)
        print(f"Welcome, {owner_name}!")
        
        # Display task statistics
        stats = self.controller.get_task_count()
        print(f"Current tasks: {stats['total']} total, {stats['uncompleted']} uncompleted")
    
    def _print_menu(self) -> None:
        """Display the main menu (Single Responsibility for menu display)."""
        print("ToDo List Manager")
        print("1. Add a task")
        print("2. View tasks")
        print("3. View overdue tasks")
        print("4. Remove a task")
        print("5. Mark task as completed")
        print("6. Edit task")
        print("7. Load tasks from DAO")
        print("8. Save tasks to DAO")
        print("9. Quit")
    
    def _handle_add_task(self) -> None:
        """Handle adding a new task with proper error handling."""
        try:
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
            
            # Check if recurring
            is_recurring_input = input("Is this a recurring task? (y/n): ").strip().lower()
            is_recurring = is_recurring_input in ['y', 'yes']
            
            interval_days = 7  # Default interval
            if is_recurring:
                try:
                    interval_input = input("Enter interval in days [default: 7]: ").strip()
                    if interval_input:
                        interval_days = int(interval_input)
                except ValueError:
                    print("Invalid interval. Using default of 7 days.")
                    interval_days = 7
            
            # Create task using controller
            success = self.controller.create_task(title, due_date, is_recurring, interval_days)
            
            if success:
                task_type = "recurring" if is_recurring else "regular"
                print(f"✓ {task_type.capitalize()} task '{title}' added successfully!")
            else:
                print("✗ Failed to create task.")
                
        except Exception as e:
            print(f"Error adding task: {e}")
    
    def _handle_view_tasks(self) -> None:
        """Handle viewing uncompleted tasks."""
        try:
            tasks = self.controller.get_uncompleted_tasks()
            
            if not tasks:
                print("No uncompleted tasks found.")
                return
            
            print("\n📋 The following tasks are still to be done:")
            print("-" * 60)
            
            all_tasks = self.controller.get_all_tasks()
            for task in tasks:
                # Get original index for display
                original_index = all_tasks.index(task) + 1
                print(f"{original_index:2d}. {task}")
                
        except Exception as e:
            print(f"Error viewing tasks: {e}")
    
    def _handle_view_overdue_tasks(self) -> None:
        """Handle viewing overdue tasks."""
        try:
            overdue_tasks = self.controller.get_overdue_tasks()
            
            if not overdue_tasks:
                print("No overdue tasks found.")
                return
            
            print("\n⚠️  Overdue tasks:")
            print("-" * 60)
            
            all_tasks = self.controller.get_all_tasks()
            for task in overdue_tasks:
                # Get original index for display
                original_index = all_tasks.index(task) + 1
                days_overdue = (datetime.datetime.now() - task.date_due).days
                print(f"{original_index:2d}. {task} (Overdue by {days_overdue} days)")
                
        except Exception as e:
            print(f"Error viewing overdue tasks: {e}")
    
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
        """Handle editing a task with proper error handling."""
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
            
            edit_choice = input("Edit (t)itle or (d)ate? ").strip().lower()
            
            if edit_choice in ['t', 'title']:
                new_title = input("Enter new title: ").strip()
                if not new_title:
                    print("Title cannot be empty.")
                    return
                
                success, message = self.controller.edit_task_title(task_num, new_title)
                
            elif edit_choice in ['d', 'date']:
                new_date_input = input("Enter new due date (YYYY-MM-DD): ").strip()
                try:
                    new_date = datetime.datetime.strptime(new_date_input, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    return
                
                success, message = self.controller.edit_task_date(task_num, new_date)
                
            else:
                print("Invalid choice. Please enter 't' for title or 'd' for date.")
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
            
            dao_type = input("Use (t)est DAO, (c)sv DAO, or (p)ickle DAO? [default: csv]: ").strip().lower()
            if dao_type not in ['t', 'test', 'c', 'csv', 'p', 'pickle']:
                dao_type = 'csv'
            
            # Map input to full type name
            type_mapping = {'t': 'test', 'c': 'csv', 'p': 'pickle'}
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
                dao_type = input("Use (t)est DAO, (c)sv DAO, or (p)ickle DAO? [default: csv]: ").strip().lower()
                if dao_type not in ['t', 'test', 'c', 'csv', 'p', 'pickle']:
                    dao_type = 'csv'
                
                # Map input to full type name
                type_mapping = {'t': 'test', 'c': 'csv', 'p': 'pickle'}
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
            
            print("Thank you for using ToDo Application!")
            print("Goodbye! 👋")
            
        except Exception as e:
            print(f"Error during quit: {e}")
            print("Goodbye!")
