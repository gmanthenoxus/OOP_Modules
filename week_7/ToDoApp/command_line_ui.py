# ui/command_line_ui.py

class CommandLineUI:
    def __init__(self, controller):
        self.controller = controller

    def _print_menu(self):
        print("\n1. Add Task\n2. Complete Task\n3. View Tasks\n4. Exit")

    def run(self):
        while True:
            self._print_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Task title: ")
                self.controller.add_task(title)
            elif choice == "2":
                try:
                    ix = int(input("Task number to complete: ")) - 1
                    self.controller.complete_task(ix)
                except (ValueError, IndexError):
                    print("Invalid index. Try again.")
            elif choice == "3":
                self.controller.view_tasks()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
