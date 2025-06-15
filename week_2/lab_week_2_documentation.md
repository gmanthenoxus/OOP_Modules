# Week 2 Lab - Python Fundamentals Documentation

## Overview

This lab demonstrates fundamental Python programming concepts essential for beginners. The code covers variables, operators, control structures, data structures, and user interaction.

## Learning Objectives

By completing this lab, students will understand:
- Variable assignment and data types
- Comparison and logical operators
- Conditional statements (if, if-else, if-elif-else)
- Lists and list operations
- Loop structures (for and while loops)
- User input and data type conversion
- Basic program structure and flow

## Code Structure

The lab is organized into 8 main sections:

1. **Variables and Comparison Operators**
2. **Demonstrating False Conditions**
3. **Logical Operators**
4. **Conditional Statements**
5. **Lists and List Operations**
6. **Loops**
7. **User Input and Data Conversion**
8. **Temperature Conversion Program**

## Section Details

### Section 1: Variables and Comparison Operators

**Purpose**: Introduce variable assignment and comparison operators.

**Code Example**:
```python
x = 24  # First number for comparison
y = 51  # Second number for comparison

a1 = x == y   # Equality: 24 == 51 → False
a2 = x != y   # Inequality: 24 != 51 → True
a3 = x > y    # Greater than: 24 > 51 → False
```

**Expected Output**:
```
Comparison Operators
Equality:  False
Inequality:  True
Greater than:  False
Less than:  True
Greater than or equal to:  False
Less than or equal to:  True
```

### Section 2: Demonstrating False Conditions

**Purpose**: Show how changing variable values affects comparison results.

**Key Concept**: By modifying the value of `x`, we can make each comparison operator return `False`.

**Examples**:
- `x = 10, y = 51`: Makes `x == y` return `False`
- `x = 51, y = 51`: Makes `x != y` return `False`
- `x = 52, y = 51`: Makes `x < y` return `False`

### Section 3: Logical Operators

**Purpose**: Demonstrate combining boolean expressions with AND, OR, and NOT.

**Code Example**:
```python
b1 = x > 10 and y < 100  # Both conditions must be True
b2 = x > 10 or y < 100   # At least one condition must be True
b3 = not(x > 10 and y < 100)  # Inverts the result
```

**Expected Output**:
```
Logical Operators
And:  True
Or:  True
Not:  False
```

### Section 4: Conditional Statements

**Purpose**: Control program flow based on conditions.

#### Simple If Statement
```python
age = 19
if age > 18:
    age_group = "adult"
    print(f"The age group is {age_group}")
```
**Output**: `The age group is adult`

#### If-Else Statement
```python
wind_speed = 30
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")
```
**Output**: `It is a windy day`

#### If-Elif-Else Statement
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
**Output**: `You passed`

### Section 5: Lists and List Operations

**Purpose**: Work with ordered collections of data.

**Basic Operations**:
```python
city_list = ["Glasgow", "London", "Edinburgh"]
print(city_list[2])        # Access by index: "Edinburgh"
print(city_list[-1])       # Negative indexing: "Edinburgh"
print(city_list[1:3])      # Slicing: ['London', 'Edinburgh']
```

**Modification Operations**:
```python
city_list.append("Manchester")     # Add to end
city_list.remove("Manchester")     # Remove first occurrence
city_list.insert(1, "Manchester")  # Insert at index
city_list[1] = "Birmingham"        # Replace at index
```

### Section 6: Loops

**Purpose**: Repeat code execution.

#### For Loop with List
```python
for city in city_list:
    print(city)
```
**Output**: Each city name on a separate line

#### For Loop with Break
```python
for i in range(5):
    if i == 2:
        break
    print(i)
```
**Output**: `0`, `1` (stops at 2)

#### While Loop
```python
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")
```
**Output**: Countdown from 10 to 1, then "Liftoff!"

### Section 7: User Input and Data Conversion

**Purpose**: Interact with users and handle different data types.

```python
user_age = int(input("Please enter your age: "))
if user_age <= 17:
    print("You are a minor")
elif user_age >= 18 and user_age < 66:
    print("You are an adult")
else:
    print("You are a senior citizen")
```

**Sample Input/Output**:
- Input: `25`
- Output: `You are an adult`

### Section 8: Temperature Conversion Program

**Purpose**: Practical application combining multiple concepts.

**Features**:
- User input for temperature and units
- Multiple conversion formulas
- Conditional logic for different conversions
- Error handling for invalid inputs

**Conversion Formulas**:
- Celsius to Fahrenheit: `(C × 9/5) + 32`
- Celsius to Kelvin: `C + 273.15`
- Fahrenheit to Celsius: `(F - 32) × 5/9`
- Fahrenheit to Kelvin: `(F - 32) × 5/9 + 273.15`
- Kelvin to Celsius: `K - 273.15`
- Kelvin to Fahrenheit: `(K - 273.15) × 9/5 + 32`

**Sample Input/Output**:
- Input: Unit: `C`, Temperature: `25`, Convert to: `F`
- Output: `25.0C is 77.0F`

## Running the Program

To run the program:
```bash
python3 lab_week_2.py
```

**Note**: The program will prompt for user input twice:
1. Age classification
2. Temperature conversion

## Key Programming Concepts Demonstrated

1. **Variables**: Storing and manipulating data
2. **Data Types**: Integers, floats, strings, booleans
3. **Operators**: Comparison (==, !=, >, <, >=, <=) and logical (and, or, not)
4. **Control Flow**: if, if-else, if-elif-else statements
5. **Data Structures**: Lists and list operations
6. **Iteration**: for and while loops
7. **User Interaction**: input() function and type conversion
8. **String Formatting**: f-strings for output formatting

## Common Errors and Solutions

1. **IndentationError**: Ensure proper indentation in code blocks
2. **TypeError**: Use appropriate type conversion (int(), float(), str())
3. **IndexError**: Check list bounds when accessing elements
4. **ValueError**: Validate user input before conversion

## Extensions and Improvements

Potential enhancements to consider:
- Add input validation for temperature conversion
- Implement case-insensitive unit input
- Add more temperature scales (Rankine, Réaumur)
- Create functions to organize code better
- Add error handling with try-except blocks
