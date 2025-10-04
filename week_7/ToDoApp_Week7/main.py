"""
Enhanced To-Do List Application - Week 7 SOLID Implementation

This version demonstrates SOLID principles and separation of concerns:

SOLID Principles Implemented:
- Single Responsibility Principle: Each class has one clear responsibility
- Open/Closed Principle: Classes are open for extension, closed for modification
- Liskov Substitution Principle: Subclasses can replace parent classes
- Interface Segregation Principle: Minimal, focused interfaces
- Dependency Inversion Principle: Depend on abstractions, not concretions

Architecture:
- UI Layer: CommandLineUI handles all user interaction
- Controller Layer: TaskManagerController handles business logic
- Model Layer: Task, TaskList, and DAO classes handle data
- Factory Pattern: TaskFactory creates appropriate task types

Features:
- Separation of concerns between UI and business logic
- Comprehensive exception handling
- Factory pattern for object creation
- Controller pattern for business logic coordination
- Clean, maintainable architecture

Author: [GLORY TITILOPE OLANREWAJU]

"""


# IMPORTS


from ui import CommandLineUI  # Import UI layer


# MAIN APPLICATION FUNCTION


def main() -> None:
    """
    Main application entry point following SOLID principles.

    This function demonstrates:
    - Single Responsibility Principle (only responsible for app startup)
    - Dependency Inversion Principle (depends on UI abstraction)
    - Separation of concerns (delegates to UI layer)

    The main function is now minimal and focused, with all complexity
    moved to appropriate layers following SOLID principles.

    Returns:
        None: Function delegates to UI layer and exits
    """
    try:
        # Create and run the UI - all complexity is properly separated
        ui = CommandLineUI()
        ui.run()

    except Exception as e:
        print(f"Fatal application error: {e}")
        print("Please restart the application.")
    except KeyboardInterrupt:
        print("\nApplication interrupted. Goodbye!")


# APPLICATION ENTRY POINT


if __name__ == "__main__":
    main()

