def add_task(task_list, task):
    task_list.append(task)
    print(f"Task '{task}' added.")

def view_tasks(task_list):
    if not task_list:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def remove_task(task_list, task_number):
    try:
        removed_task = task_list.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    except IndexError:
        print("Invalid task number.")
