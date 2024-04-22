#!/usr/bin/python3
"""
A Python script that uses a REST API to export employee TODO list data to a CSV file.
"""

import requests
import csv
import sys

if __name__ == "__main__":
  # Check for correct number of arguments
  if len(sys.argv) != 2:
    print("Usage: python3 1-export_to_CSV.py <employee_id>")
    exit(1)

  employee_id = sys.argv[1]
  url = 'https://jsonplaceholder.typicode.com/'

  # Fetch user details
  user_response = requests.get(f"{url}users/{employee_id}")
  if user_response.status_code != 200:
    print(f"Error: Unable to fetch user details for ID {employee_id}")
    exit(1)

  user_data = user_response.json()
  employee_name = user_data.get('name')

  # Fetch user's TODO list
  todos_response = requests.get(f"{url}todos?userId={employee_id}")
  if todos_response.status_code != 200:
    print(f"Error: Unable to fetch TODO list for ID {employee_id}")
    exit(1)

  tasks = todos_response.json()

  # Prepare CSV file name
  csv_filename = f"{employee_id}.csv"

  # Open CSV file for writing
  with open(csv_filename, 'w', newline='') as csvfile:
    # Create a CSV writer object
    csv_writer = csv.writer(csvfile)

    # Write header row
    header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    csv_writer.writerow(header)

    # Write data rows for each task
    for task in tasks:
      task_completed = str(task.get('completed'))  # Convert boolean to string
      data_row = [employee_id, employee_name, task_completed, task.get("title")]
      csv_writer.writerow(data_row)

  print(f"Exported employee TODO list data to: {csv_filename}")
