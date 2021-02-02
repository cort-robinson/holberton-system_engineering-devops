#!/usr/bin/python3
"""returns info about TODO list progress for given employee id"""
import requests
from sys import argv


employee_name = ((requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.format(
        argv[1]))).json()).get('name')
todos = (requests.get(
    'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1]))).json()

completed = [todo for todo in todos if todo.get('completed') is True]

print("Employee {:s} is done with tasks({}/{}):".format(
    employee_name, len(completed), len(todos)))
for task in completed:
    print("\t {:s}".format(task.get('title')))
