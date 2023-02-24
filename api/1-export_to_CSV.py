#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    user_url = f'https://jsonplaceholder.typicode.com/users/{user_id}'
    t = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    user = requests.get(user_url).json()
    todo_list = requests.get(t).json()

    completed_tasks = [task for task in todo_list if task.get('completed')]

    csv_filename = f'{user_id}.csv'

    with open(csv_filename, mode='w') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in todo_list:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user.get('username'),
                'TASK_COMPLETED_STATUS': 'True' if task.get('completed') else 'False',
                'TASK_TITLE': task.get('title')
            })
