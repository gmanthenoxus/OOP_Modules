# main.py

from tasklist import TaskList
from dao.task_test_dao import TaskTestDAO
# from dao.task_csv_dao import TaskCsvDAO  # Use this instead of TaskTestDAO for CSV

def propagate_task_list(task_list):
    dao = TaskTestDAO()
    # dao = TaskCsvDAO('tasks.csv')  # Uncomment to use real persistence
    tasks = dao.get_all_tasks()
    for task in tasks:
        task_list.add_task(task)

def main():
    task_list = TaskList()
    propagate_task_list(task_list)

    task_list.view_tasks()

if __name__ == "__main__":
    main()
