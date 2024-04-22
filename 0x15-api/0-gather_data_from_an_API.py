#!/usr/bin/python3
"""a python script that uses REST API to provide  a given employee
by their id"""

import requests

def get_todo_progress(employee_id):
  """
  Fetches TODO list progress for a given employee ID from a REST API.

  Args:
      employee_id: Integer representing the employee ID.

  Returns:
      A dictionary containing employee name, total tasks, and completed tasks, 
      or None if the request fails.
  """
  url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
  response = requests.get(url)

  if response.status_code == 200:
    user_data = response.json()
    employee_name = user_data["name"]

    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)

    if response.status_code == 200:
      todos = response.json()
      total_tasks = len(todos)
      completed_tasks = sum(todo["completed"] for todo in todos)
      return {
          "name": employee_name,
          "total_tasks": total_tasks,
          "completed_tasks": completed_tasks
      }
  
  return None

if __name__ == "__main__":
  try:
    employee_id = int(input("Enter employee ID: "))
    progress = get_todo_progress(employee_id)

    if progress:
      completed_tasks = progress["completed_tasks"]
      total_tasks = progress["total_tasks"]
      employee_name = progress["name"]
      print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
      for todo in progress:
        if todo["completed"]:
          print(f"\t{todo['title']}")
    else:
      print(f"Failed to retrieve data for employee ID: {employee_id}")
  except ValueError:
    print("Invalid input: Please enter an integer employee ID.")
