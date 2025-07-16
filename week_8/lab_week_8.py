# lab_week_8.py

from abc import ABC, abstractmethod
import random

# Task 1: Tuple Swap
def tuple_swap(a, b):
    print(f"Before: a = {a}, b = {b}")
    a, b = b, a
    print(f"After: a = {a}, b = {b}")
    return a, b

# Task 2: Set Comparison
def common_names(set1, set2):
    return set1 & set2

# Task 3: Dictionary Histogram
def histogram(lst):
    result = {}
    for item in lst:
        result[item] = result.get(item, 0) + 1
    return result

# Task 4: Abstract Dice Class and SixSidedDice
class Dice(ABC):
    @abstractmethod
    def roll(self):
        pass

class SixSidedDice(Dice):
    def roll(self):
        return random.randint(1, 6)

# Task 5: TenSidedDice
class TenSidedDice(Dice):
    def roll(self):
        return random.randint(1, 10)

# Roll Dice and collect results
def roll_dice_and_histogram(dice, rolls=1000):
    results = [dice.roll() for _ in range(rolls)]
    return histogram(results)

if __name__ == "__main__":
    # Task 1
    tuple_swap(3, 7)

    # Task 2
    set1 = {"Alice", "Bob", "Charlie"}
    set2 = {"Bob", "Diana", "Charlie"}
    print("Common names:", common_names(set1, set2))

    # Task 3
    print("Histogram of [1,2,2,3,3,3]:", histogram([1,2,2,3,3,3]))

    # Task 4
    six_dice = SixSidedDice()
    print("6-sided dice histogram:", roll_dice_and_histogram(six_dice))

    # Task 5
    ten_dice = TenSidedDice()
    print("10-sided dice histogram:", roll_dice_and_histogram(ten_dice))
