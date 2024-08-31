from core.load_save import load_tasks, save_tasks
from core.task_management import add_task, view_tasks, remove_task

def main():
    filename = "tasks.json"
    task_list = load_tasks(filename)

    while True:
        print("\nTo-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1/2/3/4): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task_list, task)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            view_tasks(task_list)
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_list, task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            save_tasks(filename, task_list)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
