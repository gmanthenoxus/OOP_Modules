# main.py

from tasklist import TaskList
from controllers.task_manager_controller import TaskManagerController
from ui.command_line_ui import CommandLineUI

def main():
    task_list = TaskList()
    controller = TaskManagerController(task_list)
    ui = CommandLineUI(controller)
    ui.run()

if __name__ == "__main__":
    main()
