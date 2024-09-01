This is a simple command-line To-Do List application built in Python. It allows users to manage their tasks by adding, viewing, and removing them. The application uses a JSON file for persistent storage, so tasks are saved between sessions.

- **`core/`**: Contains core functionality for managing tasks and file operations.
  - **`load_save.py`**: Functions to load and save tasks to a JSON file.
  - **`task_management.py`**: Functions to add, view, and remove tasks.
  - **`utils.py`**: (Optional) Additional helper functions.
- **`todo_list.py`**: The main script that provides a command-line interface for interacting with the To-Do List.
- **`tasks.json`**: JSON file used for storing tasks persistently.


## Interact with the To-Do List

1. **Add Task:** Select option 1 and enter the task description.
2. **View Tasks:** Select option 2 to see a list of current tasks.
3. **Remove Task:** Select option 3 and enter the task number to remove it.
4. **Exit:** Select option 4 to save tasks and exit the application.
