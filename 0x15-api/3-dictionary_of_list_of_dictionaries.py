#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests


def export_all_employees_todo_list_to_json():
    """
    Retrieve and export the progress of all users' to-do lists to a JSON file.

    Returns:
        None
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users_data = users_response.json()
    todos_data = todos_response.json()

    all_users_tasks = {}
    for user in users_data:
        user_tasks = []
        for task in todos_data:
            if task.get('userId') == user.get('id'):
                user_tasks.append({
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                })
        all_users_tasks[user.get('id')] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_users_tasks, jsonfile)


if __name__ == "__main__":
    export_all_employees_todo_list_to_json()
