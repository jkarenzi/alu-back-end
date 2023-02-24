#!/usr/bin/python3
"""Gather data from an API and export to CSV and JSON"""

import csv
import json
import requests
import sys

def get_user_tasks(user_id):
    """Retrieves user information and to-do list from API"""
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    tasks_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    user = requests.get(user_url).json()
    tasks = requests.get(tasks_url).json()
    return user, tasks


def export_to_csv(user, tasks):
    """Exports user tasks to a CSV file"""
    filename = '{}.csv'.format(user['id'])
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user['id'], user['username'], task['completed'], task['title']])


def export_to_json(user, tasks):
    """Exports user tasks to a JSON file"""
    filename = '{}.json'.format(user['id'])
    user_tasks = {str(user['id']): []}
    for task in tasks:
        user_task = {'task': task['title'], 'completed': task['completed'], 'username': user['username']}
        user_tasks[str(user['id'])].append(user_task)
    with open(filename, mode='w') as json_file:
        json.dump(user_tasks, json_file)


if __name__ == '__main__':
    user_id = sys.argv[1]
    user, tasks = get_user_tasks(user_id)
    export_to_csv(user, tasks)
    export_to_json(user, tasks)
