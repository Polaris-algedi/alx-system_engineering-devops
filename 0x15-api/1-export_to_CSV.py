#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def export_todo_list_to_csv(employee_id):
    """
    Retrieve and export the progress of a user's to-do list to a CSV file.

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

    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["USER_ID",
                      "USERNAME",
                      "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(csvfile,
                                fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_username,
                "TASK_COMPLETED_STATUS": task.get('completed'),
                "TASK_TITLE": task.get('title')
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_todo_list_to_csv(employee_id)
