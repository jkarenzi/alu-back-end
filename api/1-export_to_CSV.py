#!/usr/bin/python3
"""Gather data from an API and export it to CSV"""

import csv
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    t = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)

    user = requests.get(user_url).json()
    todo_list = requests.get(t).json()

    completed_tasks = [task for task in todo_list if task.get('completed')]

    with open('{}_tasks.csv'.format(user_id), mode='w') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in completed_tasks:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': user.get('name'),
                'TASK_COMPLETED_STATUS': task.get('completed'),
                'TASK_TITLE': task.get('title')
            })

    print('Exported {} completed tasks to {}_tasks.csv'.format(len(completed_tasks), user_id))
