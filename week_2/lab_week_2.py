"""
Week 2 Lab - Python Fundamentals
=================================

This lab demonstrates fundamental Python programming concepts including:
- Variables and data types
- Comparison operators (==, !=, >, <, >=, <=)
- Logical operators (and, or, not)
- Conditional statements (if, if-else, if-elif-else)
- Lists and list operations
- Loops (for, while)
- User input and basic data conversion
- Temperature conversion program

Author: [Student Name]
Date: [Date]
"""

# =============================================================================
# SECTION 1: VARIABLES AND COMPARISON OPERATORS
# =============================================================================

# Variables Definition
# Initialize two integer variables for comparison demonstrations
x = 24  # First number for comparison
y = 51  # Second number for comparison

# Comparison Operators
# These operators return Boolean values (True or False)
a1 = x == y   # Equality: checks if x equals y (24 == 51 → False)
a2 = x != y   # Inequality: checks if x is not equal to y (24 != 51 → True)
a3 = x > y    # Greater than: checks if x is greater than y (24 > 51 → False)
a4 = x < y    # Less than: checks if x is less than y (24 < 51 → True)
a5 = x >= y   # Greater than or equal: checks if x >= y (24 >= 51 → False)
a6 = x <= y   # Less than or equal: checks if x <= y (24 <= 51 → True)

# Print the results of the comparison operators
print("Comparison Operators")
print("Equality: " , a1)           # Expected output: False
print("Inequality: " ,a2)          # Expected output: True
print("Greater than: " ,a3)        # Expected output: False
print("Less than: " ,a4)           # Expected output: True
print("Greater than or equal to: " ,a5)  # Expected output: False
print("Less than or equal to: " ,a6)     # Expected output: True


# =============================================================================
# SECTION 2: DEMONSTRATING FALSE CONDITIONS
# =============================================================================

# This section demonstrates how to make each comparison operator return False
# by changing the value of x while keeping y = 51

# Making equality operator return False
x = 10  # Change x to a value different from y (51)
a1 = x == y  # 10 == 51 → False
print("Equality: where x = ", x , "and y = " , y , " the condition is" , a1)

# Making inequality operator return False
x = 51  # Change x to equal y
a2 = x != y  # 51 != 51 → False
print("Inequality: where x = ", x , "and y = " , y , " the condition is" ,a2)

# Making greater than operator return False
x = 10  # Change x to a value less than y
a3 = x > y  # 10 > 51 → False
print("Greater than:where x = ", x , "and y = " , y , " the condition is" ,a3)

# Making less than operator return False
x = 52  # Change x to a value greater than y
a4 = x < y  # 52 < 51 → False
print("Less than: where x = ", x , "and y = " , y , " the condition is" ,a4)

# Making greater than or equal operator return False
x = 10  # Change x to a value less than y
a5 = x >= y  # 10 >= 51 → False
print("Greater than or equal to: where x = ", x , "and y = " , y , " the condition is" ,a5)

# Making less than or equal operator return False
x = 58  # Change x to a value greater than y
a6 = x <= y  # 58 <= 51 → False
print("Less than or equal to: where x = ", x , "and y = " , y , " the condition is" ,a6)

# =============================================================================
# SECTION 3: LOGICAL OPERATORS
# =============================================================================

# Logical operators combine multiple boolean expressions
# Current values: x = 58, y = 51
b1 = x > 10 and y < 100  # AND: both conditions must be True (58 > 10 AND 51 < 100 → True)
b2 = x > 10 or y < 100   # OR: at least one condition must be True (58 > 10 OR 51 < 100 → True)
b3 = not(x > 10 and y < 100)  # NOT: inverts the result (NOT True → False)

# Print the results of the logical operators
print("Logical Operators")
print("And: " , b1)   # Expected output: True
print("Or: " , b2)    # Expected output: True
print("Not: " , b3)   # Expected output: False

# =============================================================================
# SECTION 4: CONDITIONAL STATEMENTS
# =============================================================================

# Conditional Statements (If)
# Simple if statement - executes code block only if condition is True

# Test 1: Age qualifies as adult (condition will be True)
age = 19
age_group = "child"  # Default value
if age > 18:  # Condition: 19 > 18 → True
    age_group = "adult"  # This line will execute
    print(f"The age group is {age_group}")  # Output: "The age group is adult"

# Test 2: Age qualifies as child (condition will be False)
age = 15
age_group = "child"  # Default value
if age > 18:  # Condition: 15 > 18 → False
    age_group = "adult"  # This line will NOT execute
    print(f"The age group is {age_group}")  # This line will NOT execute
# Note: No output for this test because condition is False

# Conditional Statements (If-Else)
# If-else provides an alternative action when condition is False

# Test 1: Wind speed above threshold (condition will be False, else executes)
wind_speed = 30
if wind_speed < 10:  # Condition: 30 < 10 → False
    print("It is a calm day")  # This will NOT execute
else:
    print("It is a windy day")  # This will execute - Output: "It is a windy day"

# Test 2: Wind speed below threshold (condition will be True, if executes)
wind_speed = 5
if wind_speed < 10:  # Condition: 5 < 10 → True
    print("It is a calm day")  # This will execute - Output: "It is a calm day"
else:
    print("It is a windy day")  # This will NOT execute

# Conditional Statements (If-Elif-Else)
# Multiple conditions checked in sequence - first True condition executes

grade = 55  # Test grade

# Grade evaluation with multiple conditions
if grade < 50:  # First condition: 55 < 50 → False, skip
    print("You failed")
elif grade < 60:  # Second condition: 55 < 60 → True, execute this block
    print("You passed")  # Output: "You passed"
elif grade < 70:  # This won't be checked since previous condition was True
    print("You got a good pass")
else:  # This won't execute since a previous condition was True
    print("You got an excellent pass")

# Compare Temperatures
# Simple comparison example
temperature_1 = 20
temperature_2 = 25

if temperature_1 == temperature_2:  # Condition: 20 == 25 → False
    print("Temperature 1 is equal to Temperature 2")
else:
    print("Temperature 1 is not equal Temperature 2")  # Output: This message

# =============================================================================
# SECTION 5: LISTS AND LIST OPERATIONS
# =============================================================================

# Lists - ordered collections of items that can be modified
city_list = ["Glasgow", "London", "Edinburgh"]  # Create list with 3 cities
print(city_list)  # Output: ['Glasgow', 'London', 'Edinburgh']

# Accessing list elements by index
print(city_list[2])   # Third element (index 2): "Edinburgh"
print(city_list[-1])  # Last element (negative indexing): "Edinburgh"

# List slicing - extracting portions of a list
print(city_list[1:3])  # Elements from index 1 to 2: ['London', 'Edinburgh']

# List modification operations
# Appending - adds element to the end
city_list.append("Manchester")
print(city_list)  # Output: ['Glasgow', 'London', 'Edinburgh', 'Manchester']

# Removing - removes first occurrence of specified element
city_list.remove("Manchester")
print(city_list)  # Output: ['Glasgow', 'London', 'Edinburgh']

# Inserting - adds element at specified index
city_list.insert(1, "Manchester")  # Insert "Manchester" at index 1
print(city_list)  # Output: ['Glasgow', 'Manchester', 'London', 'Edinburgh']

# Replacing - changes element at specified index
city_list[1] = "Birmingham"  # Replace element at index 1
print(city_list)  # Output: ['Glasgow', 'Birmingham', 'London', 'Edinburgh']

# Additional List Operations Example
colours = ["beige", "indigo", "mangenta"]  # Note: "magenta" is misspelled
print(colours)  # Output: ['beige', 'indigo', 'mangenta']

# Accessing specific list elements
print("The second item on the list is:", colours[1])  # Output: indigo

# Modifying list elements
colours[1] = "pink"  # Replace "indigo" with "pink"
print(colours)  # Output: ['beige', 'pink', 'mangenta']

# Getting list length
print("The length of the colours list is: ", len(colours))  # Output: 3

# Checking if specific value exists in list
if colours[0] == "pink" or colours[1] == "pink" or  colours[2] == "pink":
    print("Red is in the list")  # This will execute (pink is present)
else:
    print("Red is not in the list")

# List slicing to create new list
selected_colours = colours[1:3]  # Get elements from index 1 to 2
print(selected_colours)  # Output: ['pink', 'mangenta']

# =============================================================================
# SECTION 6: LOOPS
# =============================================================================

# For loop - iterating through list elements
print("\nIterating through city list:")
for city in city_list:  # Iterate through each city in the list
    print(city)  # Print each city name

# For loop with range and break statement
print("\nLoop with break at 2:")
for i in range(5):  # Loop through numbers 0 to 4
    if i == 2:  # When i equals 2
        break   # Exit the loop immediately
    print(i)    # Output: 0, 1 (stops before printing 2)

# Another for loop with break statement
print("\nLoop with break at 3:")
for i in range(5):  # Loop through numbers 0 to 4
    if i == 3:  # When i equals 3
        break   # Exit the loop immediately
    print(i)    # Output: 0, 1, 2 (stops before printing 3)

# For loop with conditional printing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nEven numbers from the list:")
for number in numbers:
    if number % 2 == 0:  # Check if number is even (remainder of division by 2 is 0)
        print(number)    # Output: 2, 4, 6, 8, 10

# For loop with accumulator pattern
sum_of_squares = 0  # Initialize accumulator
print("\nCalculating sum of squares:")
for n in range(1, 6):  # Loop through numbers 1 to 5
    sum_of_squares += n ** 2  # Add square of n to sum (n^2)
    print("The sum of squares is: ", sum_of_squares)  # Show running total
print("The sum of squares is: ", sum_of_squares)  # Final result: 55

# While loop - continues as long as condition is True
countdown = 10  # Initialize counter
print("\nCountdown sequence:")
while countdown > 0:  # Continue while countdown is greater than 0
    print(countdown)  # Print current countdown value
    countdown -= 1    # Decrease countdown by 1 (equivalent to countdown = countdown - 1)
print("Liftoff!")     # Print when loop ends (countdown reaches 0)

# =============================================================================
# SECTION 7: USER INPUT AND DATA CONVERSION
# =============================================================================

# User Input - Getting data from user and converting data types
print("\n--- Age Classification Program ---")
user_age = int(input("Please enter your age: "))  # Convert string input to integer

# Age classification using if-elif-else
if user_age <= 17:  # Minor category
    print("You are a minor")
elif user_age >= 18 and user_age < 66:  # Adult category
    print("You are an adult")
else:  # Senior citizen category (66 and above)
    print("You are a senior citizen")

# =============================================================================
# SECTION 8: TEMPERATURE CONVERSION PROGRAM
# =============================================================================

print("\n--- Temperature Conversion Program ---")
# Get user input for temperature conversion
temperature_unit = input("Please enter the temperature unit (C, F, K): ")
temperature = float(input("Please enter the temperature: "))  # Convert to float for decimal values
temperature_converter = input("Please enter the temperature unit you want to convert to (C, F, K): ")

# Temperature conversion formulas
# Celsius to Fahrenheit: (C × 9/5) + 32
# Celsius to Kelvin: C + 273.15
# Fahrenheit to Celsius: (F - 32) × 5/9
# Fahrenheit to Kelvin: (F - 32) × 5/9 + 273.15
# Kelvin to Celsius: K - 273.15
# Kelvin to Fahrenheit: (K - 273.15) × 9/5 + 32

celcius_fahrenheit = (temperature * 9/5) + 32      # C to F conversion
celcius_kelvin = temperature + 273.15              # C to K conversion
fahrenheit_celcius = (temperature - 32) * 5/9      # F to C conversion
fahrenheit_kelvin = (temperature - 32) * 5/9 + 273.15  # F to K conversion
kelvin_celcius = temperature - 273.15              # K to C conversion
kelvin_fahrenheit = (temperature - 273.15) * 9/5 + 32  # K to F conversion

# Determine which conversion to perform based on user input
if temperature_unit == "C" and temperature_converter == "F":
    print(f"{temperature}C is {celcius_fahrenheit}F")
elif temperature_unit == "C" and temperature_converter == "K":
    print(f"{temperature}C is {celcius_kelvin}K")
elif temperature_unit == "F" and temperature_converter == "C":
    print(f"{temperature}F is {fahrenheit_celcius}C")
elif temperature_unit == "F" and temperature_converter == "K":
    print(f"{temperature}F is {fahrenheit_kelvin}K")
elif temperature_unit == "K" and temperature_converter == "C":
    print(f"{temperature}K is {kelvin_celcius}C")
elif temperature_unit == "K" and temperature_converter == "F":
    print(f"{temperature}K is {kelvin_fahrenheit}F")
else:
    # Handle case where user tries to convert to same unit or invalid input
    print("You have tried to convert the same temperature unit. Please try again.")

print("\n--- End of Lab ---")

