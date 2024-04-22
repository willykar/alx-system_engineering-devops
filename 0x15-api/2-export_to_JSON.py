#!/usr/bin/python3
"""
A Python script that uses a REST API to export employee TODO list data to a CSV file
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    userID = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userID)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}"
                         .format(userID)).json()
    username = user.get('username')
    tasks = []
    for task in todos:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    json_obj = {}
    json_obj[userID] = tasks
    with open("{}.json".format(userID), 'w') as jsonfile:
        json.dump(json_obj, jsonfile)
