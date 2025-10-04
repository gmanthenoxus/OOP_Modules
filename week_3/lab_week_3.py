"""
Week 3 Lab - Functions and Error Handling


This lab demonstrates fundamental Python programming concepts including:
- Function definition and calling
- Function parameters and return values
- Input validation and error handling
- Assertions for testing
- Common Python errors and their fixes
- Mathematical calculations with functions
- List iteration and string formatting

Author: [IKENNA FRAKLIN EZEMA]
"""


# SECTION 1: BASIC FUNCTIONS WITH PARAMETERS


# Task: greet_friends
# Function that takes a list of names and greets each person
def greet_friends(friend_list):
    """
    Greets each friend in the provided list.

    Parameters:
    friend_list (list): A list of friend names to greet

    Returns:
    None (prints greetings to console)
    """
    for name in friend_list:  # Iterate through each name in the list
        print(f"Hello {name}!")  # Use f-string formatting to create personalized greeting

# Test the greet_friends function
friend_list = ["John", "Jane", "Jack"]  # Create a list of friends
greet_friends(friend_list)  # Call function with the friend list
# Expected output: Hello John!, Hello Jane!, Hello Jack!


# SECTION 2: FUNCTIONS WITH RETURN VALUES


# Task: calculate_tax
# Function that calculates tax based on income and tax rate
def calculate_tax(income, tax_rate):
    """
    Calculates tax amount based on income and tax rate.

    Parameters:
    income (float): The income amount
    tax_rate (float): The tax rate as a decimal (e.g., 0.2 for 20%)

    Returns:
    float: The calculated tax amount
    """
    return income * tax_rate  # Simple tax calculation: income × rate

# Test the calculate_tax function with different scenarios
print("Tax on £50,000 at 20% rate:", calculate_tax(50000, 0.2))  # Expected: 10000.0
print("Tax on £30,000 at 15% rate:", calculate_tax(30000, 0.15))  # Expected: 4500.0


# SECTION 3: COMPLEX FUNCTIONS WITH VALIDATION AND LOOPS


# Task: compound_interest
# Function that calculates compound interest over multiple years with input validation
def compound_interest(principal, duration, interest_rate):
    """
    Calculates compound interest over a specified duration with input validation.

    Parameters:
    principal (float): Initial investment amount
    duration (int): Number of years for the investment
    interest_rate (float): Annual interest rate as decimal (0.03 = 3%)

    Returns:
    int: Final amount after compound interest, or None if invalid input
    """
    # Input validation for interest rate
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None  # Return None to indicate invalid input

    # Input validation for duration
    if duration < 0:
        print("Please enter a positive number of years")
        return None  # Return None to indicate invalid input

    # Calculate compound interest for each year
    # Formula: A = P(1 + r)^t where A=amount, P=principal, r=rate, t=time
    for year in range(1, duration + 1):  # Loop from year 1 to duration
        total = principal * (1 + interest_rate) ** year  # Compound interest formula
        print(f"The total amount of money earned by the investment in year {year} is {total:.0f} £")

    return int(total)  # Return final amount as integer

# Test the compound_interest function
final_amount = compound_interest(1000, 5, 0.03)  # £1000 for 5 years at 3%
print("Final Amount:", final_amount)  # Expected: 1159


# SECTION 4: TESTING WITH ASSERTIONS


# Task: assertion
# Use assert to test that our function returns the expected result
assert compound_interest(1000, 5, 0.03) == 1159  # Test passes if function returns 1159
# If assertion fails, program will stop with AssertionError


# SECTION 5: COMMON PYTHON ERRORS AND FIXES


# Task: Fix common errors
# This section demonstrates common Python errors and their corrections

# Fixing Syntax Error
# Original error: Missing quotes around string
print("Hello, World!")  # Correct: String properly quoted

# Fixing Name Error
# Original error: Using undefined variable
favorite_color = "Blue"  # Define the variable first
print("My favorite color is", favorite_color)  # Now variable is defined

# Fixing Value Error
# Original error: Trying to add string and integer directly
number1 = "5"  # This is a string
number2 = 3    # This is an integer
result = int(number1) + number2  # Convert string to int before addition
print("The sum is:", result)  # Expected: 8

# Fixing Index Error
# Original error: Accessing index that doesn't exist
fruits = ["apple", "banana", "cherry"]  # List with indices 0, 1, 2
print(fruits[1])  # Access valid index (1) - Expected: "banana"

# Fixing Indentation Error
# Original error: Incorrect indentation in if statement
time = 11
if time < 12:  # Condition
    print("Good morning!")  # Correct: Properly indented code block
