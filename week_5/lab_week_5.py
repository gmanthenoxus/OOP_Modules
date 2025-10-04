"""
Week 5 Lab - Inheritance, Super(), Kwargs, and Multiple Inheritance

Demonstrates advanced OOP concepts:
- Simple and multiple inheritance
- Method overriding and polymorphism
- Super() function and **kwargs usage
- Class hierarchies and relationships

Author: [VICTOR NNAMDI EKWEMALOR]
"""

import datetime

# Simple Inheritance
class Vehicle:
    """Base vehicle class with common attributes and methods."""

    def __init__(self, colour, weight, max_speed, max_range=None, seats=None):
        self.colour = colour
        self.weight = weight
        self.max_speed = max_speed
        self.max_range = max_range
        self.seats = seats

    def move(self, speed):
        print(f"The vehicle is moving at {speed} km/h")

class Car(Vehicle):
    """Car class inheriting from Vehicle with form_factor attribute."""

    def __init__(self, colour, weight, max_speed, form_factor, max_range=None, seats=None):
        super().__init__(colour, weight, max_speed, max_range, seats)
        self.form_factor = form_factor

    def move(self, speed):
        print(f"The car is driving at {speed} km/h")

# Test simple inheritance
car = Car("blue", 1500, 250, "SUV")
car.move(150)


class Electric(Car):
    """Electric car class with battery capacity."""

    def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.battery_capacity = battery_capacity

    def move(self, speed):
        print(f"The electric car is driving at {speed} km/h")

class Petrol(Car):
    """Petrol car class with fuel capacity."""

    def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.fuel_capacity = fuel_capacity

    def move(self, speed):
        print(f"The petrol car is driving at {speed} km/h")

# Test inheritance and method overriding
electric_car = Electric("green", 1200, 200, "Hatchback", 100)
electric_car.move(100)
petrol_car = Petrol("red", 1500, 250, "SUV", 50)
petrol_car.move(150)
generic_vehicle = Vehicle("red", 1000, 200)
generic_vehicle.move(100)


# Task 1: Enhanced move method with range parameter
class ElectricTask1(Car):
    """Electric car with range-aware move method."""

    def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.battery_capacity = battery_capacity

    def move(self, speed, maximum_range):
        print(f"The electric car is driving at {speed} km/h and has a maximum range of {maximum_range} km")

class PetrolTask1(Car):
    """Petrol car with range-aware move method."""

    def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.fuel_capacity = fuel_capacity

    def move(self, speed, maximum_range):
        print(f"The petrol car is driving at {speed} km/h and has a maximum range of {maximum_range} km")

# Test enhanced move methods
electric_car_t1 = ElectricTask1("green", 1200, 200, "Hatchback", 100)
electric_car_t1.move(100, 300)
petrol_car_t1 = PetrolTask1("red", 1500, 250, "SUV", 50)
petrol_car_t1.move(150, 400)


# Task 2: Using **kwargs for flexible parameter passing
class ElectricTask2(Car):
    """Electric car demonstrating **kwargs usage."""

    def __init__(self, colour, weight, max_speed, form_factor, battery_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.battery_capacity = battery_capacity

    def move(self, speed):
        range_info = self.max_range if self.max_range else "Unknown"
        print(f"The electric car is driving at {speed} km/h and has a maximum range of {range_info} km")

class PetrolTask2(Car):
    """Petrol car demonstrating **kwargs usage."""

    def __init__(self, colour, weight, max_speed, form_factor, fuel_capacity, **kwargs):
        super().__init__(colour, weight, max_speed, form_factor, **kwargs)
        self.fuel_capacity = fuel_capacity

    def move(self, speed):
        range_info = self.max_range if self.max_range else "Unknown"
        print(f"The petrol car is driving at {speed} km/h and has a maximum range of {range_info} km")

# Test **kwargs functionality
petrol_car_t2 = PetrolTask2("red", 1500, 250, "SUV", 50, max_range=400)
petrol_car_t2.move(150)
electric_car_t2 = ElectricTask2("green", 1000, 200, "Hatchback", 100, max_range=500, seats=5)
electric_car_t2.move(100)
print(f"Electric car seats: {electric_car_t2.seats}")


# Task 3: Plane class hierarchy
class Plane(Vehicle):
    """Plane class with aviation-specific attributes."""

    def __init__(self, colour, weight, max_speed, num_engines, wingspan, **kwargs):
        super().__init__(colour, weight, max_speed, **kwargs)
        self.num_engines = num_engines
        self.wingspan = wingspan

    def move(self, speed):
        print(f"The plane is flying at {speed} km/h")

class Propeller(Plane):
    """Propeller plane with propeller specifications."""

    def __init__(self, colour, weight, max_speed, num_engines, wingspan, num_propellers, propeller_diameter, **kwargs):
        super().__init__(colour, weight, max_speed, num_engines, wingspan, **kwargs)
        self.num_propellers = num_propellers
        self.propeller_diameter = propeller_diameter

    def move(self, speed):
        print(f"The propeller plane is flying at {speed} km/h")

class Jet(Plane):
    """Jet plane with jet engine specifications."""

    def __init__(self, colour, weight, max_speed, num_engines, wingspan, num_wings, engine_thrust, **kwargs):
        super().__init__(colour, weight, max_speed, num_engines, wingspan, **kwargs)
        self.num_wings = num_wings
        self.engine_thrust = engine_thrust

    def move(self, speed):
        print(f"The jet is flying at {speed} km/h")

# Test plane hierarchy
propeller_plane = Propeller("red", 1000, 200, 2, 15, 4, 100)
propeller_plane.move(100)
jet_plane = Jet("blue", 1000, 200, 2, 20, 2, 1000)
jet_plane.move(200)
generic_plane = Plane("green", 1000, 200, 2, 10)
generic_plane.move(100)


# Multiple Inheritance: FlyingCar inherits from both Car and Plane
class FlyingCar(Car, Plane):
    """Flying car demonstrating multiple inheritance."""

    def __init__(self, colour, weight, max_speed, form_factor, wingspan, **kwargs):
        Car.__init__(self, colour, weight, max_speed, form_factor, **kwargs)
        self.wingspan = wingspan

    def move(self, speed):
        print(f"The flying car is driving or flying at {speed} km/h")

# Test multiple inheritance
generic_flying_car = FlyingCar("red", 1000, 200, "SUV", 30, seats=5)
generic_flying_car.move(100)
print(generic_flying_car.seats, generic_flying_car.wingspan, generic_flying_car.form_factor)

generic_flying_car_2 = FlyingCar(colour="red", weight=1000, max_speed=200,
                                form_factor="SUV", wingspan=30, seats=5)
generic_flying_car_2.move(100)

# Polymorphism demonstration
class Animal:
    """Simple animal class for polymorphism demonstration."""
    def move(self, speed):
        print(f"The animal is moving at a speed of {speed}")

generic_animal = Animal()
generic_animal.move(20)

# Polymorphism in action - same method name, different behaviors
for movable_object in [generic_vehicle, electric_car_t2, generic_flying_car, generic_animal]:
    movable_object.move(20)