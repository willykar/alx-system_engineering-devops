#!/usr/bin/python3
"""
Python script to export data in the JSON format
Requirements:
  Records all tasks that are owned by this employee
"""

import json
import requests
import sys


if __name__ == "__main__":
    # Get the employee id"""
    user_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information using the provided employee ID
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    # Fetch the to-do list for the employee using the provided employee ID
    params = {"userId": user_id}
    todos = requests.get(url + "todos", params).json()

    # Create a dictionary containing the user and to-do list information
    data_to_export = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    # Write the data to a JSON file with the employee ID as the filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
