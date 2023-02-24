#!/usr/bin/python3
"""Gather data from an API and export to CSV"""

import csv
import requests
import sys


def get_user_tasks(user_id):
    """Retrieves user information and to-do list from API"""
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    t_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
    user = requests.get(user_url).json()
    tasks = requests.get(t_url).json()
    return user, tasks


def export_to_csv(user, tasks):
    """Exports user tasks to a CSV file"""
    filename = str(user['id']) + '.csv'
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([user['id'], user['username'], 
            task['completed'], task['title']])


if __name__ == '__main__':
    user_id = sys.argv[1]  
    user, tasks = get_user_tasks(user_id)
    export_to_csv(user, tasks)
