"""
Week 8 Lab - Data Structures and Abstract Classes

Demonstrates Python data structures and abstract classes:
- Tuples: Immutable collections for variable swapping
- Sets: Unique element collections for intersections
- Dictionaries: Key-value pairs for frequency counting
- Abstract Classes: Blueprint classes with @abstractmethod decorator
- Polymorphism through abstract class inheritance

Author: [MOSES GANA]
"""

from abc import ABC, abstractmethod
import random
from typing import Dict, List, Set, Tuple, Any

# EXERCISE 1: TUPLES - Variable Swapping

def tuple_swap(a: Any, b: Any) -> Tuple[Any, Any]:
    """Swap two variables using tuple packing/unpacking."""
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a  # Tuple unpacking for swap
    print(f"After swap: a = {a}, b = {b}")
    return a, b

def demonstrate_tuple_operations() -> None:
    """Demonstrate various tuple operations and use cases."""

    # Multiple variable swap
    x, y, z = 1, 2, 3
    print(f"Before rotation: x={x}, y={y}, z={z}")
    x, y, z = z, x, y  # Rotate values
    print(f"After rotation: x={x}, y={y}, z={z}")

    # Tuple unpacking with functions
    def get_name_age():
        return "Alice", 25

    name, age = get_name_age()
    print(f"Unpacked from function: {name}, {age}")

    # Tuple as immutable data structure
    coordinates = (10.5, 20.3)
    print(f"Coordinates (immutable): {coordinates}")

# EXERCISE 2: SETS - Finding Common Elements

def common_names(set1: Set[str], set2: Set[str]) -> Set[str]:
    """Find names that appear in both sets using intersection."""
    return set1 & set2  # Set intersection operator

def demonstrate_set_operations() -> None:
    """Demonstrate comprehensive set operations."""

    # Given sets from the exercise
    set1 = {"Tom", "Jerry", "Hewey", "Dewey", "Louie"}
    set2 = {"Tom", "Garfield", "Snoopy", "Hewey", "Dewey"}

    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")

    # Various set operations
    print(f"Intersection (common): {set1 & set2}")
    print(f"Union (all unique): {set1 | set2}")
    print(f"Difference (only in set1): {set1 - set2}")
    print(f"Symmetric difference (not in both): {set1 ^ set2}")

    # Set methods
    print(f"Is Tom in set1? {('Tom' in set1)}")
    print(f"Set1 subset of union? {set1.issubset(set1 | set2)}")

# EXERCISE 3: DICTIONARIES - Histogram Function

def histogram(lst: List[Any]) -> Dict[Any, int]:
    """Create histogram dictionary counting frequency of each element."""
    result = {}
    for item in lst:
        result[item] = result.get(item, 0) + 1
    return result

def test_histogram_function() -> None:
    """Test the histogram function with various data types."""
    print("=== Histogram Function Testing ===")

    # Test with provided example
    test_list = [1, 2, 3, 1, 2, 3, 4]
    result = histogram(test_list)
    expected = {1: 2, 2: 2, 3: 2, 4: 1}

    print(f"Input: {test_list}")
    print(f"Result: {result}")
    print(f"Expected: {expected}")

    # Assertion test
    assert result == expected, f"Test failed: {result} != {expected}"
    print("✓ Basic histogram test passed!")

    # Test with strings
    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
    word_hist = histogram(words)
    print(f"Word histogram: {word_hist}")

    # Test with mixed types
    mixed = [1, "hello", 1, "world", "hello", 2.5, 2.5]
    mixed_hist = histogram(mixed)
    print(f"Mixed type histogram: {mixed_hist}")

# EXERCISE 4: ABSTRACT CLASSES - Dice Implementation

class Dice(ABC):
    """Abstract base class for dice objects demonstrating @abstractmethod decorator."""

    def __init__(self) -> None:
        """Initialize dice with no face value."""
        self.face: int = None

    @abstractmethod
    def roll(self) -> int:
        """Abstract method to roll dice - must be implemented by subclasses."""
        pass

    def get_face(self) -> int:
        """Get current face value."""
        return self.face

    def __str__(self) -> str:
        """String representation of dice."""
        return f"{self.__class__.__name__}(face={self.face})"

class SixSidedDice(Dice):
    """Six-sided dice implementation of abstract Dice class."""

    def roll(self) -> int:
        """Roll six-sided dice returning 1-6."""
        self.face = random.randint(1, 6)
        return self.face

class TenSidedDice(Dice):
    """Ten-sided dice implementation demonstrating polymorphism."""

    def roll(self) -> int:
        """Roll ten-sided dice returning 1-10."""
        self.face = random.randint(1, 10)
        return self.face

def roll_dice_and_histogram(dice: Dice, rolls: int = 1000) -> Dict[int, int]:
    """
    Roll dice multiple times and create a histogram of results.

    Args:
        dice: Dice object to roll
        rolls: Number of times to roll (default: 1000)

    Returns:
        Dict[int, int]: Histogram of roll results
    """
    results = [dice.roll() for _ in range(rolls)]
    return histogram(results)

def test_dice_implementations() -> None:
    """Test dice classes and demonstrate polymorphism."""
    print("=== Abstract Dice Class Testing ===")

    # Test SixSidedDice
    print("Testing SixSidedDice:")
    six_dice = SixSidedDice()
    six_histogram = roll_dice_and_histogram(six_dice, 1000)
    print(f"Six-sided dice histogram (1000 rolls): {six_histogram}")

    # Verify all faces 1-6 are present
    expected_faces = set(range(1, 7))
    actual_faces = set(six_histogram.keys())
    assert actual_faces == expected_faces, f"Missing faces: {expected_faces - actual_faces}"
    print("✓ Six-sided dice test passed!")

    # Test TenSidedDice
    print("\nTesting TenSidedDice:")
    ten_dice = TenSidedDice()
    ten_histogram = roll_dice_and_histogram(ten_dice, 1000)
    print(f"Ten-sided dice histogram (1000 rolls): {ten_histogram}")

    # Verify all faces 1-10 are present
    expected_faces = set(range(1, 11))
    actual_faces = set(ten_histogram.keys())
    assert actual_faces == expected_faces, f"Missing faces: {expected_faces - actual_faces}"
    print("✓ Ten-sided dice test passed!")

    # Demonstrate polymorphism
    print("\nDemonstrating Polymorphism:")
    dice_collection = [SixSidedDice(), TenSidedDice()]

    for dice_obj in dice_collection:
        result = dice_obj.roll()
        print(f"{dice_obj.__class__.__name__} rolled: {result}")
        print(f"Current state: {dice_obj}")

def demonstrate_abstract_class_enforcement() -> None:
    """Demonstrate that abstract classes cannot be instantiated."""
    print("=== Abstract Class Enforcement ===")

    try:
        # This should raise TypeError
        abstract_dice = Dice()
        print("ERROR: Abstract class was instantiated!")
    except TypeError as e:
        print(f"✓ Abstract class correctly prevented instantiation: {e}")

    # Show that concrete classes work fine
    concrete_dice = SixSidedDice()
    print(f"✓ Concrete class instantiated successfully: {concrete_dice}")

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
