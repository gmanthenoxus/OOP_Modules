"""
Week 6 Lab - Debugging and Error Handling

This lab contains intentional errors for debugging practice:
- Type hint errors (speed should be int, not str)
- Logic errors (division by zero potential)
- Missing error handling for edge cases

Students should identify and fix these errors while learning:
- Proper type hints and data types
- Exception handling with try-except blocks
- Edge case validation

Author: [MOSES GANA]
"""

class Car:
    """Car class with intentional bugs for debugging practice."""

    def __init__(self, speed: str = 0) -> None:  # Bug: speed should be int, not str
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def accelerate(self) -> None:
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self) -> None:  # Bug: extra space in type hint
        self.odometer += self.speed
        self.time += 1

    def average_speed(self) -> float:
        return self.odometer / self.time  # Bug: potential division by zero


if __name__ == '__main__':
    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("What should I do? [A]ccelerate, [B]rake, "
                        "show [O]dometer, or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
            print("Accelerating...")
        elif action == 'B':
            my_car.brake()
            print("Braking...")
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            # Bug: No error handling for division by zero when time = 0
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()