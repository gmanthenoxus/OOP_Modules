# Week 5 - Advanced OOP Concepts

## Overview
This week focuses on advanced Object-Oriented Programming concepts including inheritance, polymorphism, method overriding, and encapsulation.

## Project Structure

### 1. Basic Lab (`lab_week_5.py`)
Comprehensive demonstration of inheritance and polymorphism concepts.

**[MARKDOWN DOCUMENTATION NEEDED: Inheritance and Polymorphism Guide]**
- Simple inheritance (Vehicle → Car)
- Method overriding and super() usage
- **kwargs for flexible parameter passing
- Multiple inheritance (FlyingCar)
- Polymorphism demonstration

### 2. Enhanced ToDoApp (`ToDoAppWeek5/`)
Practical application of OOP concepts in a real project.

**Files:**
- `main.py` - Enhanced application with recurring task support
- `task.py` - Task and RecurringTask classes demonstrating inheritance
- `tasklist.py` - TaskList with encapsulation via get_task method

**[MARKDOWN DOCUMENTATION NEEDED: OOP Implementation Guide]**
- Inheritance implementation (RecurringTask extends Task)
- Polymorphic method overriding (mark_as_completed)
- Encapsulation principles (get_task method)
- Professional OOP design patterns

## Key OOP Concepts Demonstrated

### Inheritance
- **Base Classes**: Vehicle, Task
- **Derived Classes**: Car, Electric, Petrol, Plane, RecurringTask
- **Constructor Chaining**: Using super().__init__()
- **Method Inheritance**: Inheriting parent methods

### Polymorphism
- **Method Overriding**: Different move() implementations
- **Runtime Behavior**: Same method name, different behaviors
- **Practical Example**: RecurringTask.mark_as_completed()

### Encapsulation
- **Controlled Access**: get_task() method instead of direct access
- **Data Protection**: Private methods (_compute_next_due_date)
- **Interface Design**: Clean public methods

### Multiple Inheritance
- **Diamond Problem**: FlyingCar inherits from Car and Plane
- **Constructor Conflicts**: Manual initialization approach
- **Method Resolution**: Understanding inheritance order

## Running the Applications

### Basic Lab
```bash
python lab_week_5.py
```

### Enhanced ToDoApp
```bash
cd ToDoAppWeek5
python main.py
```

## Learning Progression

**[MARKDOWN DOCUMENTATION NEEDED: OOP Learning Path]**
1. **Simple Inheritance** - Basic parent-child relationships
2. **Method Overriding** - Customizing inherited behavior
3. **Polymorphism** - Same interface, different implementations
4. **Multiple Inheritance** - Complex inheritance hierarchies
5. **Encapsulation** - Controlled access to data

## Week 5 Requirements Met

Based on the course memories, Week 5 specifically requires:

### ✅ Polymorphism Implementation
- **RecurringTask.mark_as_completed()** overrides parent method
- Updates due dates using polymorphism
- Different behavior for recurring vs regular tasks

### ✅ Encapsulation Enhancement
- **get_task() method** in TaskList for proper encapsulation
- Replaces direct tasks list access
- Demonstrates controlled data access

### ✅ Class Hierarchies
- **User and Owner classes** with __str__ methods
- **TaskList with Owner attribute** 
- **Proper inheritance patterns** throughout

**[MARKDOWN DOCUMENTATION NEEDED: Requirements Compliance Guide]**
- Detailed explanation of polymorphism implementation
- Encapsulation best practices demonstration
- Class relationship diagrams
- Code quality assessment criteria

## Assessment Integration

**[MARKDOWN DOCUMENTATION NEEDED: Week 5 Assessment Guide]**
- OOP concept evaluation rubric
- Inheritance implementation standards
- Polymorphism demonstration requirements
- Encapsulation principle application
- Code organization and documentation standards

---

**Note**: This README identifies key areas where comprehensive markdown documentation would enhance understanding of advanced OOP concepts and their practical implementation.
