#!/usr/bin/python3
""" A Python script to export data in the CSV format"""
import csv
import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]

    # Fetch user data
    user_response = requests.get(f"{url}users/{user_id}")
    if user_response.status_code != 200:
        print(f"Error: unable to fetch user details for ID {user_id}")
        sys.exit(1)
        
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Fetch user's TODO list
    todos_response = requests.get(f"{url}todos?userId={user_id}")
    if todos_response.status_code != 200:
        print(f"Error: unable to fetch TODO list for ID {user_id}")
        sys.exit(1)
        
    todos_data = todos_response.json()

    # Prepare data for CSV
    csv_data = []
    for todo in todos_data:
        completed_status = "True" if todo['completed'] else "False"
        task_title = todo['title']
        csv_data.append([user_id, employee_name, completed_status, task_title])

    # Write data to CSV file
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(csv_data)

    print(f"CSV file '{csv_filename}' has been created successfully.")
