#!/usr/bin/python3
"""returns info about TODO list progress for given employee id"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    username = ((requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            argv[1]))).json()).get('username')
    todos = (requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            argv[1]))).json()

    with open('{}.csv'.format(argv[1]), 'w') as f:
        f_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            f_writer.writerow([todo.get('userId'),
                               username,
                               todo.get('completed'),
                               todo.get('title')
                               ])
