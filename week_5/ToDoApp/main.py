# main.py
from task_list import TaskList
from users import Owner

def main():
    print("Welcome to the ToDoApp Portfolio Task Manager!")
    name = input("Enter owner's name: ")
    email = input("Enter owner's email: ")
    owner = Owner(name, email)

    todo = TaskList(owner)

    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Get Specific Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            task = input("Enter task to remove: ")
            todo.remove_task(task)
        elif choice == "3":
            print(f"\n{todo}")
        elif choice == "4":
            try:
                index = int(input("Enter task number: ")) - 1
                task = todo.get_task(index)
                if task:
                    print(f"Task {index + 1}: {task}")
                else:
                    print("Task not found.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
