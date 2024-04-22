#!/usr/bin/python3
"""
A Python script to export data in the JSON format
Requirements:
    Records all tasks from all employees
"""

import json
import requests
import sys


if __name__ == "__main__":
    root = "https://jsonplaceholder.typicode.com"
    users = requests.get(root + "/users")
    for names in users.json():
        usr_id = names.get('id')
        todo = requests.get(root + "/todos", params={"userId": usr_id})
        csv_arr = []
        for tasks in todo.json():
            csv_arr.append({"task": tasks.get("title"),
                            "completed": str(tasks.get("completed")),
                            "username": names.get("name")})
        with open("todo_all_employees.json", 'a') as f:
            f.write(json.dumps({usr_id: csv_arr}))
