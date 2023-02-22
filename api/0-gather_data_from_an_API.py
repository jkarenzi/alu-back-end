#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TO DO list progress.
"""

import json
import requests
import sys


if __name__ == "__main__":
    """
    Define the base URL for the API
    """
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    """
    Get the employee ID from the command line arguments
    """
    if len(sys.argv) != 2:
        print('Usage: python todo.py EMPLOYEE_ID')
        sys.exit(1)
    employee_id = int(sys.argv[1])

    """ 
    Make a request to get the employee name
    """
    response = requests.get(f'{BASE_URL}/users/{employee_id}')
    if response.status_code != 200:
        print(f'Error: Could not retrieve employee name for ID {employee_id}')
        sys.exit(1)
    employee_name = response.json()['name']

    """ 
    Make a request to get the employee's TO DO list
    """
    response = requests.get(f'{BASE_URL}/todos', params={'userId': employee_id})
    if response.status_code != 200:
        print(f'Error: Could not retrieve TODO list for employee {employee_name}')
        sys.exit(1)
    todos = response.json()

    """
    Calculate the number of completed tasks and the total number of tasks
    """
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todos)

    """
    Print the employee TO DO list progress
    """
    print(f'Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):')
    for todo in completed_tasks:
        print(f'\t{todo["title"]}')
