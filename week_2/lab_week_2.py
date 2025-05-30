# Week 2 Lab

# Variables Definition
x = 24
y = 51

# Comparison Operators
a1 = x == y
a2 = x != y
a3 = x > y
a4 = x < y
a5 = x >= y
a6 = x <= y

# Print the results of the comparison operators
print("Comparison Operators")
print("Equality: " , a1)
print("Inequality: " ,a2)
print("Greater than: " ,a3)
print("Less than: " ,a4)
print("Greater than or equal to: " ,a5)
print("Less than or equal to: " ,a6)


# Print Result to make all Comparison Operators False
x = 10
a1 = x == y

print("Equality: where x = ", x , "and y = " , y , " the condition is" , a1)
x=51
a2 = x != y

print("Inequality: where x = ", x , "and y = " , y , " the condition is" ,a2)
x = 10
a3 = x > y

print("Greater than:where x = ", x , "and y = " , y , " the condition is" ,a3)
x=52
a4 = x < y

print("Less than: where x = ", x , "and y = " , y , " the condition is" ,a4)
x = 10
a5 = x >= y

print("Greater than or equal to: where x = ", x , "and y = " , y , " the condition is" ,a5)
x=58
a6 = x <= y
print("Less than or equal to: where x = ", x , "and y = " , y , " the condition is" ,a6)

# Logical Operators
b1 = x > 10 and y < 100
b2 = x > 10 or y < 100
b3 = not(x > 10 and y < 100)

# Print the results of the logical operators
print("Logical Operators")
print("And: " , b1)
print("Or: " , b2)
print("Not: " , b3)


# Conditional Statements (If)
# Test 1 With adult result
age = 19
age_group = "child"
if age > 18:
    age_group = "adult"
    print(f"The age group is {age_group}")

# Test 2 With child result
age = 15
age_group = "child"
if age > 18:
    age_group = "adult"
    print(f"The age group is {age_group}")


# Conditional Statements (If-Else)
# Test 1 With speed above threshold
wind_speed = 30
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

# Test 2 With speed below threshold
wind_speed = 5
if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

# Conditional Statements (If-Elif-Else)

grade = 55

if grade < 50:
    print("You failed")
elif grade < 60:
    print("You passed")
elif grade < 70:
    print("You got a good pass")
else:
    print("You got an excellent pass")

# Compare Temperatures

temperature_1 = 20
temperature_2 = 25

if temperature_1 == temperature_2:
    print("Temperature 1 is equal to Temperature 2")
else:
    print("Temperature 1 is not equal Temperature 2")


# Lists
city_list = ["Glasgow", "London", "Edinburgh"]
print(city_list)

# Print the third element of the list
print(city_list[2])
print(city_list[-1])

# Print last 2 items of a list using slcing
print(city_list[1:3])

# appending to lists
city_list.append("Manchester")
print(city_list)

# removing from lists
city_list.remove("Manchester")
print(city_list)

# inserting into lists
city_list.insert(1, "Manchester")
print(city_list)

# replacing items in lists
city_list[1] = "Birmingham"
print(city_list)

# Access, Create and Modify Lists
colours = ["beige", "indigo", "mangenta"]
print(colours)

print("The second item on the list is:", colours[1])

colours[1] = "pink"
print(colours)

print("The length of the colours list is: ", len(colours))

if colours[0] == "pink" or colours[1] == "pink" or  colours[2] == "pink":
    print("Red is in the list")
else:
    print("Red is not in the list")

selected_colours = colours[1:3]
print(selected_colours)

# Loops

for city in city_list:
    print(city)

for i in range(5):
    if i == 2:
        break
    print(i)


for i in range(5):
    if i == 3:
        break
    print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print(number)

sum_of_squares = 0

for n in range(1,6):
    sum_of_squares += n ** 2
    print("The sum of squares is: ", sum_of_squares)
print("The sum of squares is: ", sum_of_squares)

countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Liftoff!")

#User Input

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


#convert celcius to fahrenheit and kelvin
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
