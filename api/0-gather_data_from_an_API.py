#!/usr/bin/python3
"""Gather data from an API"""

import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)

    user = requests.get(user_url).json()
    todo_list = requests.get(todo_url).json()

    completed_tasks = [task for task in todo_list if task.get('completed')]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todo_list)

    print('Employee {} is done with tasks({}/{}):'
          .format(user.get('name'), num_completed_tasks, total_num_tasks))

    for task in completed_tasks:
        print('\t {}'.format(task.get('title')))
