#!/usr/bin/python3
"""
This script retrieves information about a given employee's TO DO list progress
using the provided REST API.

Modules:
    - requests: HTTP library for making requests to the API
    - sys: system-specific parameters and functions

Usage:
    python todo.py EMPLOYEE_ID

Arguments:
    EMPLOYEE_ID: integer ID of the employee to retrieve TO DO list progress for

Dependencies:
    - requests: can be installed via pip

Output:
    The script outputs information about the employee's TO DO list progress in this
    exact format:
    First line: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    EMPLOYEE_NAME: name of the employee
    NUMBER_OF_DONE_TASKS: number of completed tasks
    TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed and non-completed tasks
    Second and N next lines display the title of completed tasks: TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

Examples:
    python todo.py 1
    Employee Leanne Graham is done with tasks(12/20):
            sunt aut facere repellat provident occaecati excepturi optio reprehenderit
            ... (list of completed task titles)
"""

import requests
import sys

# Define the base URL for the API
BASE_URL = 'https://jsonplaceholder.typicode.com'

# Get the employee ID from the command line arguments
if len(sys.argv) != 2:
    print('Usage: python todo.py EMPLOYEE_ID')
    sys.exit(1)
employee_id = int(sys.argv[1])

# Make a request to get the employee name
response = requests.get(f'{BASE_URL}/users/{employee_id}')
if response.status_code != 200:
    print(f'Error: Could not retrieve employee name for ID {employee_id}')
    sys.exit(1)
employee_name = response.json()['name']

# Make a request to get the employee's TODO list
response = requests.get(f'{BASE_URL}/todos', params={'userId': employee_id})
if response.status_code != 200:
    print(f'Error: Could not retrieve TODO list for employee {employee_name}')
    sys.exit(1)
todos = response.json()

# Calculate the number of completed tasks and the total number of tasks
completed_tasks = [todo for todo in todos if todo['completed']]
num_completed_tasks = len(completed_tasks)
total_num_tasks = len(todos)

# Print the employee TODO list progress
print(f'Employee {employee_name} is done with tasks({num_completed_tasks}/{total_num_tasks}):')
for todo in completed_tasks:
    print(f'\t{todo["title"]}')
