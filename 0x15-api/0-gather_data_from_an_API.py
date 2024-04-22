#!/usr/bin/python3
"""A Python script that uses a REST API to retrieve information about an employee by their ID."""

import requests
from sys import argv

if __name__ == "__main__":
  # Check for correct number of arguments
  if len(argv) != 2:
    print("Usage: python3 script.py <employee_id>")
    exit(1)

  employee_id = argv[1]

  # Fetch user details
  user_response = requests.get(
      f"https://jsonplaceholder.typicode.com/users/{employee_id}")
  if user_response.status_code != 200:
    print(f"Error: Unable to fetch user details for ID {employee_id}")
    exit(1)

  user_data = user_response.json()
  employee_name = user_data.get('name')

  # Fetch user's TODO list
  todos_response = requests.get(
      f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
  if todos_response.status_code != 200:
    print(f"Error: Unable to fetch TODO list for ID {employee_id}")
    exit(1)

  todos_data = todos_response.json()

  # Calculate completed tasks (more concise way)
  completed_count = sum(todo['completed'] for todo in todos_data)
  total_tasks = len(todos_data)

  # Display employee TODO list progress
  print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
  for task in todos_data:
    if task['completed']:
      print(f"\t{task['title']}")
