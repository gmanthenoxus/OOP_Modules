Week 2 – Operators, Conditions, Lists, Loops, and User Input

This lab demonstrates the use of comparison operators, logical operators, conditionals, lists, loops, and user input in Python.


# Comparison Operators -
Comparison operators are used to compare two values and return a Boolean result (True or False).

**Example** 
```python
x = 24
y = 51

a1 = x == y
a2 = x != y
a3 = x > y
a4 = x < y
a5 = x >= y
a6 = x <= y

print("Comparison Operators")
print("Equality: " , a1)
print("Inequality: " ,a2)
print("Greater than: " ,a3)
print("Less than: " ,a4)
print("Greater than or equal to: " ,a5)
print("Less than or equal to: " ,a6)
```

**Output:**
```console
Comparison Operators
Equality: False
Inequality: True
Greater than: False
Less than: True
Greater than or equal to: False
Less than or equal to: True
```


## Making All Comparison Operators False


**Example**
```python
x = 10
a1 = x == y
print("Equality: where x =", x , "and y =", y , "the condition is", a1)

x = 51
a2 = x != y
print("Inequality: where x =", x , "and y =", y , "the condition is", a2)

x = 10
a3 = x > y
print("Greater than: where x =", x , "and y =", y , "the condition is", a3)

x = 52
a4 = x < y
print("Less than: where x =", x , "and y =", y , "the condition is", a4)

x = 10
a5 = x >= y
print("Greater than or equal to: where x =", x , "and y =", y , "the condition is", a5)

x = 58
a6 = x <= y
print("Less than or equal to: where x =", x , "and y =", y , "the condition is", a6)
```
The Comparison Opertors will show in the output of the code 

**output**
 ``` console 
 Equality:  False
Inequality:  True
Greater than:  False
Less than:  True
Greater than or equal to:  False
Less than or equal to:  True 
```

# Logical Operators 

Logical operations in Python are used to combine conditional statements using and, or, and not to return Boolean values.

**Example**
 
```python
b1 = x > 10 and y < 100
b2 = x > 10 or y < 100
b3 = not(x > 10 and y < 100) 

print("Logical Operators")
print("And: ", b1)
print("Or: ", b2)
print("Not: ", b3)
```
If both conditions in an and operation are not true, the overall result is false because and requires all conditions to be true.

here is what the output will look like 
**Output**
```
And:  True
Or:  True
Not:  False
```

# Conditional Statements (If, If-Else, If-Elif-Else)

Conditional Statements let the program make decisions by executing code blocks based on whether conditions are true or false.


**Examples**
```python
# If Statement
age = 19
age_group = "child"
if age > 18:
    age_group = "adult"
    print(f"The age group is {age_group}")


age = 15
age_group = "child"
if age > 18:
    age_group = "adult"
    print(f"The age group is {age_group}")
```

```python
# If-Else Statement
wind_speed = 30
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

wind_speed = 5
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")
```

```python
# If-Elif-Else
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

The outputs for the above Examples will be 
**Example1**
 ```Console 
 The age group is adult
```

**Example2**
```console
It is a windy day
It is a calm day
```

**Example3**
``` console
You passed
```



## Comparing Temperatures

**Example**
```python
temperature_1 = 20
temperature_2 = 25

if temperature_1 == temperature_2:
    print("Temperature 1 is equal to Temperature 2")
else:
    print("Temperature 1 is not equal Temperature 2")
```
**Output**
```
Temperature 1 is not equal Temperature 2
```

# Lists and List Operations
Lists are ordered collections of items that can be modified, accessed, and manipulated using various operations.


## Some Examples Includes: 


**Example1**
```python 
city_list = ["Glasgow", "London", "Edinburgh"]
print(city_list)
print(city_list[2])
print(city_list[-1])
print(city_list[1:3])
city_list.append("Manchester")
print(city_list)
city_list.remove("Manchester")
print(city_list)
city_list.insert(1, "Manchester")
print(city_list)
city_list[1] = "Birmingham"
print(city_list)
```
**Output**
```Console
['Glasgow', 'London', 'Edinburgh']
Edinburgh
Edinburgh
['London', 'Edinburgh']
['Glasgow', 'London', 'Edinburgh', 'Manchester']
['Glasgow', 'London', 'Edinburgh']
['Glasgow', 'Manchester', 'London', 'Edinburgh']
['Glasgow', 'Birmingham', 'London', 'Edinburgh']
```

**Example2**
```python
colours = ["beige", "indigo", "mangenta"]
print(colours)
print("The second item on the list is:", colours[1])
colours[1] = "pink"
print(colours)
print("The length of the colours list is:", len(colours))

if colours[0] == "pink" or colours[1] == "pink" or colours[2] == "pink":
    print("Red is in the list")
else:
    print("Red is not in the list")

selected_colours = colours[1:3]
print(selected_colours)
```
**Output**
``` console 
['beige', 'indigo', 'mangenta']
The second item on the list is: indigo
['beige', 'pink', 'mangenta']
The length of the colours list is: 3
Red is in the list
['pink', 'mangenta']
```

# Loops
Loops are programming structures that repeat a block of code multiple times until a condition is met.

## Examples 

**Example1 Looping through a list**
(this will print each city one after the other)

```python
for city in city_list: 
    print(city)
```
**Output**
```console
Glasgow
London
Edinburgh
```

**Example 2 For loop with break**
Prints numbers 0 and 1, then stops the loop when i equals 2
```python
for i in range(5):
    if i == 2:
        break
    print(i)
```

**Output**
```console
0
1
```

**Example 3**
Prints numbers 0, 1, and 2, then stops the loop when i equals 3
```python 
for i in range(5):
    if i == 3:
        break
    print(i)
```
**Output**
```Console
0
1
2
```
**Example 4: To print even numbers from a list**
Prints all even numbers from the list of the numbers
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(number)
```

**Example 5 Calculate and prints the running total of squares of numbers 1 to 5**

Calculates and prints the running total of squares of numbers 1 to 5

```python 
sum_of_squares = 0
for n in range(1, 6):
    sum_of_squares += n ** 2
    print("The sum of squares is:", sum_of_squares)
print("The sum of squares is:", sum_of_squares)
```

**Output**
```Console
The sum of squares is: 1
The sum of squares is: 5
The sum of squares is: 14
The sum of squares is: 30
The sum of squares is: 55
The sum of squares is: 55
```
**Example 4: Prints all even numbers from the list numbers**
```python
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")
```


# User Input and Temperature Conversion
User Input and Temperature Conversion means getting a temperature value from the user and converting it from one unit to another (e.g., Celsius to Fahrenheit). It shows how to handle input and perform calculations in a program.

```python
user_age = int(input("Please enter your age: "))
if user_age <= 17:
    print("You are a minor")
elif user_age >= 18 and user_age < 66:
    print("You are an adult")
else:
    print("You are a senior citizen")

temperature_unit = input("Please enter the temperature unit (C, F, K): ")
temperature = float(input("Please enter the temperature: "))
temperature_converter = input("Please enter the temperature unit you want to convert to (C, F, K): ")

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
elif temperature_unit == "F" and temperature_converter == "C":
    print(f"{temperature}F is {fahrenheit_celcius}C")
elif temperature_unit == "F" and temperature_converter == "K":
    print(f"{temperature}F is {fahrenheit_kelvin}K")
elif temperature_unit == "K" and temperature_converter == "C":
    print(f"{temperature}K is {kelvin_celcius}C")
elif temperature_unit == "K" and temperature_converter == "F":
    print(f"{temperature}K is {kelvin_fahrenheit}F")
else:
    print("You have tried to convert the same temperature unit. Please try again.")
```

## Result of the Program 
When the user runs the program, they will first be asked to enter their age, and the program will tell them if they are a minor, adult, or senior citizen. Then, the program will ask for a temperature value and its unit, plus the unit they want to convert it to, and it will display the converted temperature or an error message if the same units are chosen.

# Week 3
Week 3 – Functions, Return Values, Assertions, and Error Fixing in Python

This week, you will learn how to:  
- Create reusable blocks of code using functions  
- Use parameters and return values  
- Perform validations with assertions  
- Identify and fix common programming errors

These concepts help build robust, reusable, and maintainable Python programs.

# Task 1: Greeting Friends with a Function
Explanation:
Functions are reusable code blocks that keep your code organized and clean. This function, greet_friends, takes a list of names and prints a friendly message for each one.

# Task 1 Greet Friends 
This function loops through a list of names and prints a greeting for each friend.


**Example:**
```python
def greet_friends(friend_list):
    for name in friend_list:
        print(f"Hello {name}!")

friend_list = ["John", "Jane", "Jack"]
greet_friends(friend_list)
```

**Output:**
The output prints a greeting for each name in the friend_list 

Console
```Hello John!
Hello Jane!
Hello Jack!
```
# Task 2: Calculating Tax
This function calculates tax based on income and tax rate. Functions return values using the return keyword.


**Example:**

```python
def calculate_tax(income, tax_rate):
    return income * tax_rate

print("Tax on £50,000 at 20% rate:", calculate_tax(50000, 0.2))
print("Tax on £30,000 at 15% rate:", calculate_tax(30000, 0.15))
```
## This function calculates tax by multiplying income with the tax rate, then prints the result for two different incomes.

**Output:**
Console 
```Tax on £50,000 at 20% rate: 10000.0  
Tax on £30,000 at 15% rate: 4500.0
```

# Task 3: Compound Interest Calculation
This function calculates how money grows with annually compounded interest. It includes input validation to ensure valid interest rate and duration.

**Example:**
```python
def compound_interest(principal, duration, interest_rate):
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    if duration < 0:
        print("Please enter a positive number of years")
        return None

    for year in range(1, duration + 1):
        total = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {total:.0f} £")

    return int(total)

final_amount = compound_interest(1000, 5, 0.03)
print("Final Amount:", final_amount)
```
This function calculates how an investment grows each year with compound interest, printing the total per year and returning the final amount.

**Output:**
Console 
```
The total amount of money earned by the investment in year 1 is 1030 £  
The total amount of money earned by the investment in year 2 is 1061 £  
The total amount of money earned by the investment in year 3 is 1093 £  
The total amount of money earned by the investment in year 4 is 1126 £  
The total amount of money earned by the investment in year 5 is 1159 £  
Final Amount: 1159
```
# Task 4: Assertion (Function Validation)
An assertion checks if a function gives the expected result. If it's correct, nothing happens; if it's wrong, it raises an AssertionError.

**Example**
```python
assert compound_interest(1000, 5, 0.03) == 1159
```
- If the assertion is correct, no output appears.  
- If incorrect, it raises an AssertionError.

**Output**
console
``` no output
```
or 
```
AssertionError
```

# Task 5: Fixing Common Errors
 Syntax Error happens when the code violates Python’s rules, like missing a colon or parentheses, preventing the program from running.

**Examples and their outputs :**
1. Syntax Error
```python
print("Hello, World!")
```
Console
```
Hello, World!
```

2. Name Error
```python
favorite_color = "Blue"
print("My favorite color is", favorite_color)
```

Console
```
My favorite color is Blue
```

3. Value Error
```python
number1 = "5"
number2 = 3
result = int(number1) + number2
print("The sum is:", result)
```

Console
```
The sum is: 8
```

 4. Index Error
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
```

Console
```
banana
```

5. Indentation Error
```python
time = 11
if time < 12:
    print("Good morning!")
```
Console
```
Good morning
```

## Summary
Example 1 runs without any error and prints Hello, World!. Example 2 prints the favorite color message: My favorite color is Blue. Example 3 converts a string to an integer, adds it to another number, and outputs The sum is: 8. Example 4 accesses the second element of the list and prints banana. Example 5 checks a condition and prints Good morning!.



