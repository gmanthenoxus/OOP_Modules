# Task: greet_friends
def greet_friends(friend_list):
    for name in friend_list:
        print(f"Hello {name}!")

friend_list = ["John", "Jane", "Jack"]
greet_friends(friend_list)

# Task: calculate_tax
def calculate_tax(income, tax_rate):
    return income * tax_rate

print("Tax on £50,000 at 20% rate:", calculate_tax(50000, 0.2))

# Try different values
print("Tax on £30,000 at 15% rate:", calculate_tax(30000, 0.15))


# Task: compound_interest
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

# Test call
final_amount = compound_interest(1000, 5, 0.03)
print("Final Amount:", final_amount)

# Task: assertion
assert compound_interest(1000, 5, 0.03) == 1159

# Task: Fix common errors

# Fixing Syntax Error
print("Hello, World!")

# Fixing Name Error
favorite_color = "Blue"
print("My favorite color is", favorite_color)

# Fixing Value Error
number1 = "5"
number2 = 3
result = int(number1) + number2
print("The sum is:", result)

# Fixing Index Error
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# Fixing Indentation Error
time = 11
if time < 12:
    print("Good morning!")
