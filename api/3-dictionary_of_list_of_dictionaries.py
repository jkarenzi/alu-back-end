#!/usr/bin/python3
"""Gather data from an API and export to CSV and JSON"""

import csv
import json
import requests
import sys


def get_all_user_tasks():
    """Retrieves information and to-do list for all users from API"""
    user_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(user_url).json()
    all_tasks = {}
    for user in users:
        tasks_url = (
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user['id'])
        )
        tasks = requests.get(tasks_url).json()
        all_tasks[str(user['id'])] = []
        for task in tasks:
            task_data = {
                'username': user['username'],
                'task': task['title'],
                'completed': task['completed']
            }
            all_tasks[str(user['id'])].append(task_data)
    return all_tasks


def export_to_csv(user, tasks):
    """Exports user tasks to a CSV file"""
    filename = '{}.csv'.format(user['id'])
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
                user['id'], user['username'], task['completed'], task['title']
            ])


def export_to_json(all_tasks):
    """Exports user tasks to a JSON file"""
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == '__main__':
    all_tasks = get_all_user_tasks()
    export_to_json(all_tasks)
