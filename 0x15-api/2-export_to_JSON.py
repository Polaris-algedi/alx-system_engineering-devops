#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
import sys


def export_todo_list_to_json(employee_id):
    """
    Retrieve and export the progress of a user's to-do list to a JSON file.

    Args:
        employee_id (int): The ID of the employee whose to-do
        list progress is to be checked.

    Returns:
        None
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"{user_url}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    employee_username = user_data.get('username')

    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_username
        })

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump({employee_id: tasks}, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_todo_list_to_json(employee_id)
