#!/usr/bin/python3
"""returns info about TODO list progress for given employee id"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    username = ((requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            argv[1]))).json()).get('username')
    todos = (requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            argv[1]))).json()

    new_dict = {'{}'.format(argv[1]): [{"task": todo.get('title'),
                                        "completed": todo.get('completed'),
                                        "username": username
                                        }
                                       for todo in todos]}

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(new_dict, f)
