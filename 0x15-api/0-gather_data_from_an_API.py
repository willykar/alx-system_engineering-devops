#!/usr/bin/python3
"""a python script that uses REST API to provide  a given employee
by their id"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        exit(1)

    employee_id = argv[1]

user_response =
requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
if user_response.status_code != 200:
    print(f"Errot: unable to fetch user details for ID {employee_id}")
    exit(1)

user_data = user_response.json()
employee_name = user_data.get('name')

# Fetch user's TODo list
todos_response =
requests.
get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
if todos_response.status_code != 200:
    print(f"Error: unable to fetch TODO list for ID {employee_id}")
    exit(1)

todos_data = todos_response.json()

# Calculate completed tasks
completed_tasks = [todo for todo in todos_data if todo['completed']]
total_tasks = len(todos_data)
completed_count = len(completed_tasks)

# Display employee TODO list
print(f"Employee {employee_name} is done with
      tasks({completed_count}/{total_tasks}):")
for task in completed_tasks:
    print(f"{task['title']}")
