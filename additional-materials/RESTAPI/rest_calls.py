import requests

# get all tasks
response = requests.get('http://127.0.0.1:5000/tasks')
print(response.json())

# create a new task
response = requests.post('http://127.0.0.1:5000/tasks', json={'title': 'Read a book'})
print(response.json())

# update a task
response = requests.put('http://127.0.0.1:5000/tasks/1', json={'title': 'Buy groceries', 'done': True})
print(response.json())

# delete a task
response = requests.delete('http://127.0.0.1:5000/tasks/2')
print(response.json())
