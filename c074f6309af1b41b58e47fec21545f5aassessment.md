# Week 2

## Section 1: Variables and Comparison Operators

Week 2 introduces fundamental programming concepts including variables, operators, control structures, and data manipulation. The lab demonstrates practical applications of these concepts through various exercises.

### Exercise 1: Basic Comparison Operations

The lab begins with variable assignment and comparison operators to understand how Python evaluates conditions.

```python
# Variables Definition
x = 24  # First number for comparison
y = 51  # Second number for comparison

# Comparison Operators
a1 = x == y   # Equality: 24 == 51 → False
a2 = x != y   # Inequality: 24 != 51 → True
a3 = x > y    # Greater than: 24 > 51 → False
a4 = x < y    # Less than: 24 < 51 → True
a5 = x >= y   # Greater than or equal: 24 >= 51 → False
a6 = x <= y   # Less than or equal: 24 <= 51 → True
```

Output when run:
```console
Comparison Operators
Equality:  False
Inequality:  True
Greater than:  False
Less than:  True
Greater than or equal to:  False
Less than or equal to:  True
```

### Exercise 2: Demonstrating False Conditions

This exercise shows how changing variable values affects comparison results, demonstrating the dynamic nature of variables.

```python
# Making equality operator return False
x = 10  # Change x to a value different from y (51)
a1 = x == y  # 10 == 51 → False

# Making inequality operator return False
x = 51  # Change x to equal y
a2 = x != y  # 51 != 51 → False
```

Output when run:
```console
Equality: where x =  10 and y =  51  the condition is False
Inequality: where x =  51 and y =  51  the condition is False
```

## Section 2: Logical Operators

Logical operators combine multiple boolean expressions, essential for complex decision-making in programs.

```python
# Current values: x = 58, y = 51
b1 = x > 10 and y < 100  # AND: both conditions must be True
b2 = x > 10 or y < 100   # OR: at least one condition must be True
b3 = not(x > 10 and y < 100)  # NOT: inverts the result
```

Output when run:
```console
Logical Operators
And:  True
Or:  True
Not:  False
```

## Section 3: Conditional Statements

### Exercise 1: Simple If Statements

```python
# Test 1: Age qualifies as adult
age = 19
age_group = "child"  # Default value
if age > 18:  # Condition: 19 > 18 → True
    age_group = "adult"
    print(f"The age group is {age_group}")
```

Output when run:
```console
The age group is adult
```

### Exercise 2: If-Else Statements

```python
# Wind speed example
wind_speed = 30
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")
```

Output when run:
```console
It is a windy day
```

### Exercise 3: If-Elif-Else Statements

```python
grade = 55
if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")
```

Output when run:
```console
You passed
```

## Section 4: Lists and List Operations

Lists are fundamental data structures in Python for storing ordered collections of items.

### Exercise 1: Basic List Operations

```python
# Creating and accessing lists
city_list = ["Glasgow", "London", "Edinburgh"]
print(city_list)  # Output: ['Glasgow', 'London', 'Edinburgh']

# Accessing elements
print(city_list[2])   # Third element: "Edinburgh"
print(city_list[-1])  # Last element: "Edinburgh"

# List slicing
print(city_list[1:3])  # Elements from index 1 to 2: ['London', 'Edinburgh']
```

### Exercise 2: List Modification

```python
# Appending - adds element to the end
city_list.append("Manchester")
print(city_list)  # Output: ['Glasgow', 'London', 'Edinburgh', 'Manchester']

# Removing - removes first occurrence
city_list.remove("Manchester")
print(city_list)  # Output: ['Glasgow', 'London', 'Edinburgh']

# Inserting - adds element at specified index
city_list.insert(1, "Manchester")
print(city_list)  # Output: ['Glasgow', 'Manchester', 'London', 'Edinburgh']

# Replacing - changes element at specified index
city_list[1] = "Birmingham"
print(city_list)  # Output: ['Glasgow', 'Birmingham', 'London', 'Edinburgh']
```

### Exercise 3: List Analysis

```python
colours = ["beige", "indigo", "mangenta"]
print("The second item on the list is:", colours[1])  # Output: indigo

colours[1] = "pink"
print("The length of the colours list is: ", len(colours))  # Output: 3

# Checking for specific values
if colours[0] == "pink" or colours[1] == "pink" or colours[2] == "pink":
    print("Red is in the list")  # This executes since pink is present
```

## Section 5: Loops

### Exercise 1: For Loops with Lists

```python
# Iterating through list elements
for city in city_list:
    print(city)
```

Output when run:
```console
Glasgow
Birmingham
London
Edinburgh
```

### Exercise 2: For Loops with Range and Break

```python
# Loop with break statement
for i in range(5):
    if i == 2:
        break
    print(i)
```

Output when run:
```console
0
1
```

### Exercise 3: Conditional Processing in Loops

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:  # Check if even
        print(number)
```

Output when run:
```console
2
4
6
8
10
```

### Exercise 4: Accumulator Pattern

```python
sum_of_squares = 0
for n in range(1, 6):
    sum_of_squares += n ** 2
    print("The sum of squares is: ", sum_of_squares)
```

Output when run:
```console
The sum of squares is:  1
The sum of squares is:  5
The sum of squares is:  14
The sum of squares is:  30
The sum of squares is:  55
```

### Exercise 5: While Loops

```python
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")
```

Output when run:
```console
10
9
8
7
6
5
4
3
2
1
Liftoff!
```

## Section 6: User Input and Data Conversion

### Exercise 1: Age Classification Program

```python
user_age = int(input("Please enter your age: "))
if user_age <= 17:
    print("You are a minor")
elif user_age >= 18 and user_age < 66:
    print("You are an adult")
else:
    print("You are a senior citizen")
```

Sample Input/Output:
```console
Please enter your age: 45
You are an adult
```

### Exercise 2: Temperature Conversion Program

A comprehensive program demonstrating multiple concepts working together:

```python
temperature_unit = input("Please enter the temperature unit (C, F, K): ")
temperature = float(input("Please enter the temperature: "))
temperature_converter = input("Please enter the temperature unit you want to convert to (C, F, K): ")

# Temperature conversion formulas
celcius_fahrenheit = (temperature * 9/5) + 32
celcius_kelvin = temperature + 273.15
fahrenheit_celcius = (temperature - 32) * 5/9
fahrenheit_kelvin = (temperature - 32) * 5/9 + 273.15
kelvin_celcius = temperature - 273.15
kelvin_fahrenheit = (temperature - 273.15) * 9/5 + 32

if temperature_unit == "C" and temperature_converter == "F":
    print(f"{temperature}C is {celcius_fahrenheit}F")
elif temperature_unit == "C" and temperature_converter == "K":
    print(f"{temperature}C is {celcius_kelvin}K")
# ... additional conversion cases
```

Sample Input/Output:
```console
Please enter the temperature unit (C, F, K): C
Please enter the temperature: 25
Please enter the temperature unit you want to convert to (C, F, K): F
25.0C is 77.0F
```

## Key Programming Concepts Demonstrated in Week 2

1. **Variables and Data Types**: Integer, float, string, boolean
2. **Comparison Operators**: ==, !=, >, <, >=, <=
3. **Logical Operators**: and, or, not
4. **Control Flow**: if, if-else, if-elif-else statements
5. **Data Structures**: Lists and list operations (append, remove, insert, slicing)
6. **Iteration**: for loops, while loops, break statements
7. **User Interaction**: input() function and type conversion
8. **String Formatting**: f-strings for output formatting
9. **Mathematical Operations**: Basic arithmetic and compound calculations

<hr/>

# Week 3

## Section 1: Introduction to Functions

Week 3 focuses on function definition, parameters, return values, and error handling. Functions are essential for code organization, reusability, and modularity.

### Exercise 1: Basic Function with Parameters

```python
def greet_friends(friend_list):
    """
    Greets each friend in the provided list.

    Parameters:
    friend_list (list): A list of friend names to greet
    """
    for name in friend_list:
        print(f"Hello {name}!")

# Test the function
friend_list = ["John", "Jane", "Jack"]
greet_friends(friend_list)
```

Output when run:
```console
Hello John!
Hello Jane!
Hello Jack!
```

### Exercise 2: Functions with Return Values

```python
def calculate_tax(income, tax_rate):
    """
    Calculates tax amount based on income and tax rate.

    Parameters:
    income (float): The income amount
    tax_rate (float): The tax rate as a decimal

    Returns:
    float: The calculated tax amount
    """
    return income * tax_rate

print("Tax on £50,000 at 20% rate:", calculate_tax(50000, 0.2))
print("Tax on £30,000 at 15% rate:", calculate_tax(30000, 0.15))
```

Output when run:
```console
Tax on £50,000 at 20% rate: 10000.0
Tax on £30,000 at 15% rate: 4500.0
```

## Section 2: Complex Functions with Validation

### Exercise 1: Compound Interest Calculator with Input Validation

```python
def compound_interest(principal, duration, interest_rate):
    """
    Calculates compound interest with input validation.
    Formula: A = P(1 + r)^t
    """
    # Input validation
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None

    # Calculate compound interest for each year
    for year in range(1, duration + 1):
        total = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {total:.0f} £")

    return int(total)

# Test the function
final_amount = compound_interest(1000, 5, 0.03)
print("Final Amount:", final_amount)
```

Output when run:
```console
The total amount of money earned by the investment in year 1 is 1030 £
The total amount of money earned by the investment in year 2 is 1061 £
The total amount of money earned by the investment in year 3 is 1093 £
The total amount of money earned by the investment in year 4 is 1126 £
The total amount of money earned by the investment in year 5 is 1159 £
Final Amount: 1159
```

## Section 3: Testing with Assertions

### Exercise 1: Function Testing

```python
# Use assert to test function returns expected result
assert compound_interest(1000, 5, 0.03) == 1159
```

This assertion tests that our compound interest function returns the correct value. If the assertion fails, the program will stop with an AssertionError, indicating a bug in our function.

## Section 4: Error Handling and Common Python Errors

### Exercise 1: Common Error Types and Fixes

```python
# Fixing Syntax Error - Missing quotes
print("Hello, World!")  # Correct: String properly quoted

# Fixing Name Error - Undefined variable
favorite_color = "Blue"  # Define variable first
print("My favorite color is", favorite_color)

# Fixing Value Error - Type conversion
number1 = "5"  # String
number2 = 3    # Integer
result = int(number1) + number2  # Convert string to int
print("The sum is:", result)

# Fixing Index Error - Invalid list index
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Access valid index

# Fixing Indentation Error - Proper code block indentation
time = 11
if time < 12:
    print("Good morning!")  # Properly indented
```

Output when run:
```console
Hello, World!
My favorite color is Blue
The sum is: 8
banana
Good morning!
```

## Section 5: Interactive Console Application

### Exercise 1: To-Do List Manager

A complete interactive program demonstrating advanced concepts:

```python
# Global data structure
tasks = []

def add_task():
    """Add a task to the list"""
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks():
    """Display all current tasks"""
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    """Remove a task by number with error handling"""
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Task '{removed}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program loop
while True:
    print("\nTo-Do List Manager")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
```

Sample Program Interaction:
```console
To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 1
Enter the task you want to add: Buy groceries
Task 'Buy groceries' added.

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Quit
Enter your choice: 2
Current tasks:
1. Buy groceries
```

## Key Programming Concepts Demonstrated in Week 3

1. **Function Definition**: Creating reusable code blocks with def keyword
2. **Function Parameters**: Passing data into functions for processing
3. **Return Values**: Functions returning calculated results
4. **Input Validation**: Checking user input for validity before processing
5. **Error Handling**: Using try-except blocks to handle runtime errors
6. **Assertions**: Testing function behavior with assert statements
7. **Global Variables**: Sharing data across functions
8. **Interactive Programs**: Creating menu-driven console applications
9. **List Manipulation**: Advanced list operations with user interaction
10. **Program Flow Control**: While loops for continuous program execution
11. **String Formatting**: Advanced f-string usage for user feedback
12. **Mathematical Calculations**: Implementing financial formulas in code

## Advanced Concepts Introduced

### Function Documentation
- **Docstrings**: Multi-line strings describing function purpose and parameters
- **Type Hints**: Indicating expected parameter and return types in comments
- **Parameter Documentation**: Describing what each parameter represents

### Error Types and Handling
- **SyntaxError**: Incorrect Python syntax
- **NameError**: Using undefined variables
- **ValueError**: Invalid value for operation (e.g., converting non-numeric string to int)
- **IndexError**: Accessing invalid list indices
- **IndentationError**: Incorrect code block indentation

### Program Architecture
- **Modular Design**: Breaking programs into focused functions
- **Separation of Concerns**: Each function has a single responsibility
- **User Interface Design**: Creating intuitive menu systems
- **Data Persistence**: Maintaining program state throughout execution

### Best Practices Demonstrated
- **Input Validation**: Always check user input before processing
- **Error Messages**: Provide clear, helpful error messages
- **Function Documentation**: Document function purpose and usage
- **Code Organization**: Group related functionality together
- **User Feedback**: Confirm actions and provide status updates

<hr/>

# Week 4

## Section 1: Object-Oriented Programming and Classes

Week 4 introduces Object-Oriented Programming (OOP) concepts, focusing on classes, objects, methods, and code organization. This week demonstrates the transition from procedural to object-oriented programming paradigms.

### Exercise 1: Basic Class Definition and Instantiation

```python
class TaskList:
    """
    A class to represent a task list with an owner and collection of tasks.

    Attributes:
        owner (str): The name of the task list owner (title case)
        tasks (list): A list of Task objects
    """

    def __init__(self, owner: str) -> None:
        """Constructor method - initializes a new TaskList instance."""
        self.owner = owner.title()  # Convert to title case
        self.tasks = []  # Initialize empty list

    def add_task(self, task: 'Task') -> None:
        """Adds a task to the task list."""
        self.tasks.append(task)
        print(f"Task '{task}' added.")

# Create an instance (object) of the TaskList class
task_list = TaskList("john doe")
print(f"Welcome {task_list.owner}")  # Output: Welcome John Doe
```

### Exercise 2: Enhanced Task Class with Special Methods

```python
class Task:
    """Represents an individual task with title, dates, and completion status."""

    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        """Initialize a new Task instance."""
        self.title = title
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.completed = False

    def __str__(self) -> str:
        """String representation of the Task object."""
        status = "[Completed]" if self.completed else "[Not Completed]"
        return f"{self.title} {status} Created: {self.date_created} Due: {self.date_due}"

    def mark_as_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True
        print(f"Task '{self.title}' is completed.")
```

Sample Program Interaction:
```console
Enter the name of the owner: momo
Welcome Momo

To-Do List Manager
1. Add a task
2. View tasks
3. Remove a task
4. Mark task as completed
5. Edit task
6. Quit
Enter your choice: 1
Enter the task you want to add: swim
Enter a due date (YYYY-MM-DD): 2025-10-23
Task 'swim [Not Completed] Created: 2025-06-15 22:00:27.343566 Due: 2025-10-23 00:00:00' added.

To-Do List Manager
Enter your choice: 2
Current tasks:
1. swim [Not Completed] Created: 2025-06-15 22:00:27.343566 Due: 2025-10-23 00:00:00
```

## Section 2: Code Modularization and Imports

### Exercise 1: Separating Classes into Modules

**File Structure:**
```
ToDoApp/
├── main.py        # Main application logic
├── task.py        # Task class definition
└── task_list.py   # TaskList class definition
```

**task.py - Task Module:**
```python
"""
Task Module - Object-Oriented Task Management
"""
import datetime

class Task:
    def __init__(self, title: str, date_due: datetime.datetime) -> None:
        self.title = title
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.completed = False

    def __str__(self) -> str:
        status = "[Completed]" if self.completed else "[Not Completed]"
        return f"{self.title} {status} Created: {self.date_created} Due: {self.date_due}"
```

**task_list.py - TaskList Module:**
```python
"""
TaskList Module - Task Collection Management
"""
from task import Task  # Import Task class from task module

class TaskList:
    def __init__(self, owner: str) -> None:
        self.owner = owner.title()
        self.tasks: list[Task] = []  # Type hint with generic

    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
        print(f"Task '{task}' added.")
```

**main.py - Main Application:**
```python
"""
Main Application Module - Modularized To-Do List Manager
"""
from task_list import TaskList  # Import from task_list module
from task import Task           # Import from task module
import datetime

def main() -> None:
    input_owner = input("Enter the name of the owner: ")
    task_list = TaskList(input_owner)
    # Application logic continues...

if __name__ == "__main__":
    main()
```

## Section 3: Type Hints and Type Checking

### Exercise 1: Function Type Hints

```python
def propagate_task_list(task_list: TaskList) -> TaskList:
    """
    Populate a task list with sample tasks for testing purposes.

    Args:
        task_list (TaskList): The task list to populate with sample data

    Returns:
        TaskList: The same task list instance with added sample tasks
    """
    task_list.add_task(Task("Buy groceries", datetime.datetime.now()))
    return task_list
```

### Exercise 2: Class Attribute Type Hints

```python
class TaskList:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner.title()
        self.tasks: list[Task] = []  # Generic type hint

    def add_task(self, task: Task) -> None:
        """Type hints specify expected parameter and return types."""
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        """Type hints improve code documentation and IDE support."""
        try:
            del self.tasks[ix]
        except IndexError:
            print("Please enter a valid number.")
```

## Section 4: Enhanced Portfolio Project

### Exercise 1: Extended Task Class with Descriptions

```python
class Task:
    """Enhanced Task class with description support."""

    def __init__(self, title: str, date_due: datetime.datetime, description: str) -> None:
        self.title = title
        self.date_created = datetime.datetime.now()
        self.date_due = date_due
        self.completed = False
        self.description = description  # Enhanced feature

    def __str__(self) -> str:
        status = "[Completed]" if self.completed else "[Not Completed]"
        return f"{self.title} {status} Created: {self.date_created} Due: {self.date_due} Description: {self.description}"

    def change_description(self, new_description: str) -> None:
        """Enhanced method for changing task description."""
        self.description = new_description
        print(f"Task description changed to '{self.description}'")
```

### Exercise 2: Advanced TaskList with Overdue Filtering

```python
class TaskList:
    """Enhanced TaskList with overdue task filtering."""

    def view_overdue_tasks(self) -> None:
        """Display only overdue tasks with numbering."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Overdue tasks:")
            overdue_count = 0

            for i, task in enumerate(self.tasks, start=1):
                if task.date_due < datetime.datetime.now():
                    print(f"{i}. {task}")
                    overdue_count += 1

            if overdue_count == 0:
                print("No overdue tasks found.")
```

Sample Enhanced Application Interaction:
```console
To-Do List Manager - Portfolio Edition
1. Add a task
2. View tasks
3. View overdue tasks
4. Remove a task
5. Mark task as completed
6. Edit task
7. Quit
Enter your choice: 1
Enter the task you want to add: Complete project
Enter a due date (YYYY-MM-DD): 2024-01-15
Would you like to add a description? (y/n): y
Enter the description: Finish the portfolio project for OOP module
Task 'Complete project [Not Completed] Created: ... Due: 2024-01-15 Description: Finish the portfolio project for OOP module' added.

Enter your choice: 3
Overdue tasks:
1. Complete project [Not Completed] Created: ... Due: 2024-01-15 Description: Finish the portfolio project for OOP module
```

## Section 5: Error Handling and Exception Management

### Exercise 1: Comprehensive Error Handling

```python
def main() -> None:
    while True:
        try:
            # Application logic here
            choice = input("Enter your choice: ")
            if choice == "1":
                # Task creation with date parsing
                input_date = input("Enter a due date (YYYY-MM-DD): ")
                date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")

        except ValueError:  # Handle invalid number conversions and date parsing
            print("Please enter a valid number or date format (YYYY-MM-DD).")
        except IndexError:  # Handle invalid list indices
            print("Please enter a valid task number.")
        except Exception as e:  # Handle any other unexpected errors
            print(f"An error occurred: {e} Please try again.")
```

### Exercise 2: Class-Level Error Handling

```python
class TaskList:
    def remove_task(self, ix: int) -> None:
        """Remove a task with proper error handling."""
        try:
            my_task = self.tasks[ix]
            del self.tasks[ix]
            print(f"Task '{my_task}' removed.")
        except IndexError:  # Handle invalid index gracefully
            print("Please enter a valid number.")
```
## Key Programming Concepts Demonstrated in Week 4

### Object-Oriented Programming Fundamentals
1. **Classes and Objects**: Defining blueprints and creating instances
2. **Constructor Methods**: `__init__` method for object initialization
3. **Instance Attributes**: Data stored within object instances
4. **Instance Methods**: Functions that operate on object data
5. **Special Methods**: `__str__` for string representation
6. **Encapsulation**: Bundling data and methods together

### Advanced OOP Concepts
1. **Type Hints**: Specifying parameter and return types
2. **Generic Types**: `list[Task]` for type-safe collections
3. **Method Documentation**: Comprehensive docstrings
4. **Class Composition**: TaskList containing Task objects
5. **Data Validation**: Input checking and error handling

### Code Organization and Modularization
1. **Module Structure**: Separating classes into different files
2. **Import Statements**: Bringing functionality from other modules
3. **Dependency Management**: Understanding module relationships
4. **Code Separation**: UI logic separate from data classes
5. **Professional Structure**: Organized file hierarchy

### Type Checking and Documentation
1. **Function Type Hints**: Parameter and return type specification
2. **Class Attribute Types**: Explicit type declarations
3. **Generic Type Hints**: `list[Task]` for collection types
4. **Documentation Standards**: Professional docstring formatting
5. **Code Comments**: Comprehensive inline documentation

### Error Handling and Robustness
1. **Exception Hierarchy**: Specific to general error handling
2. **Graceful Degradation**: Continuing operation after errors
3. **User Feedback**: Clear error messages and guidance
4. **Input Validation**: Checking data before processing
5. **Defensive Programming**: Anticipating potential issues

### Professional Development Practices
1. **Code Documentation**: Module, class, and method documentation
2. **Type Safety**: Using type hints for better code quality
3. **Error Handling**: Comprehensive exception management
4. **Code Organization**: Logical separation of concerns
5. **User Experience**: Intuitive interfaces and feedback

## Portfolio Project Features

### Basic Version (ToDoApp/)
- **Modular Structure**: Separate files for different classes
- **Type Hints**: Complete type annotation
- **Error Handling**: Comprehensive exception management
- **Professional Documentation**: Detailed docstrings and comments

### Enhanced Version (ToDoAppPortfolio/)
- **Extended Functionality**: Task descriptions and overdue filtering
- **Advanced Features**: Enhanced editing capabilities
- **Professional UI**: Improved user interface design
- **Portfolio Quality**: Production-ready code standards

## Development Progression

### From Procedural to Object-Oriented
- **Week 2-3**: Procedural programming with functions
- **Week 4**: Object-oriented programming with classes
- **Encapsulation**: Data and behavior bundled together
- **Reusability**: Classes can be instantiated multiple times
- **Maintainability**: Organized code structure

### From Single File to Modular
- **Single File**: All code in one file (lab_week_4.py)
- **Modular**: Separated into multiple files (ToDoApp/)
- **Enhanced**: Additional features (ToDoAppPortfolio/)
- **Professional**: Production-ready structure and documentation

### Code Quality Evolution
- **Basic**: Working functionality
- **Documented**: Comprehensive comments and docstrings
- **Typed**: Complete type hint coverage
- **Robust**: Comprehensive error handling
- **Professional**: Portfolio-quality implementation

<hr/>

