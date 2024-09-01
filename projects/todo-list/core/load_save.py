import json
import os

def load_tasks(filename):
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            json.dump([], file, indent=4)
    
    # Load tasks from the file
    with open(filename, 'r') as file:
        tasks = json.load(file)
    
    return tasks

def save_tasks(filename, task_list):
    with open(filename, 'w') as file:
        json.dump(task_list, file, indent=4)
