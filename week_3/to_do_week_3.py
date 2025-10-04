
"""
Week 3 To-Do List Manager - Interactive Console Application


This program demonstrates advanced Python concepts including:
- Interactive user input and menu systems
- List manipulation and management
- Function organization and modularity
- Error handling with try-except blocks
- While loops for continuous program execution
- Conditional logic for menu navigation
- String formatting and user feedback

This is a complete console-based to-do list manager that allows users to:
- Add tasks to their list
- View all current tasks
- Remove specific tasks by number
- Exit the program gracefully

Author: [IKENNA FRAKLIN EZEMA]
"""


# GLOBAL DATA STRUCTURE


# Initialize an empty list to store tasks
# This list will persist throughout the program execution
tasks = []  # Global list to store all user tasks


# FUNCTION DEFINITIONS


# Function to add a task to the list
def add_task():
    """
    Prompts user for a task description and adds it to the global tasks list.

    Returns:
    None (modifies global tasks list and prints confirmation)
    """
    task = input("Enter the task you want to add: ")  # Get task from user
    tasks.append(task)  # Add task to the global tasks list
    print(f"Task '{task}' added.")  # Confirm task was added

# Function to view current tasks in the list
def view_tasks():
    """
    Displays all current tasks in a numbered list format.
    Shows "No tasks" message if list is empty.

    Returns:
    None (prints task list to console)
    """
    if not tasks:  # Check if tasks list is empty
        print("No tasks in the list.")
    else:
        print("Current tasks:")
        # Use enumerate to get both index and task, starting numbering from 1
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")  # Display task number and description

# Function to remove a task from the list
def remove_task():
    """
    Allows user to remove a task by selecting its number.
    Includes error handling for invalid input and out-of-range numbers.

    Returns:
    None (modifies global tasks list and prints confirmation)
    """
    view_tasks()  # First show current tasks so user can see numbers
    if not tasks:  # If no tasks exist, exit function early
        return

    try:  # Error handling for invalid input
        task_number = int(input("Enter the task number to remove: "))

        # Check if the entered number is within valid range
        if 1 <= task_number <= len(tasks):
            # Remove task at specified index (subtract 1 for 0-based indexing)
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed}' removed.")  # Confirm removal
        else:
            print("Invalid task number.")  # Number out of range

    except ValueError:  # Handle case where user enters non-numeric input
        print("Please enter a valid number.")


# MAIN PROGRAM LOOP


# Main program loop - continues until user chooses to quit
while True:  # Infinite loop until break statement
    # Display menu options
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")  # Get user's menu selection

    # Process user choice using if-elif-else structure
    if choice == "1":
        add_task()  # Call function to add a task
    elif choice == "2":
        view_tasks()  # Call function to view all tasks
    elif choice == "3":
        remove_task()  # Call function to remove a task
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break  # Exit the while loop and end program
    else:
        print("Invalid choice. Please try again.")  # Handle invalid menu choice


