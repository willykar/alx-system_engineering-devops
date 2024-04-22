#!/usr/bin/python3
import json
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

    # Prepare data for JSON
    json_data = {user_id: []}
    for todo in todos_data:
        completed_status = todo['completed']
        task_title = todo['title']
        json_data[user_id].append({'task': task_title, 'completed': completed_status, 'username': employee_name})

    # Write data to JSON file
    json_filename = f"{user_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print(f"JSON file '{json_filename}' has been created successfully.")
