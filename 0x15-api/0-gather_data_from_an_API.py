#!/usr/bin/python3
"""
	API DATA
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch user data
        user_response = requests.get(user_url)
        user_data = user_response.json()
        
        # Fetch TODO list data
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Extract completed tasks
        completed_tasks = [task['title'] for task in todos_data if task['completed']]

        # Display information
        print(f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{len(todos_data)}):")
        print(f"\t{user_data['name']}: name of the employee")
        print(f"\t{len(completed_tasks)}: number of completed tasks")
        print(f"\t{len(todos_data)}: total number of tasks")

        # Display completed tasks
        for task_title in completed_tasks:
            print(f"\t{task_title}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

