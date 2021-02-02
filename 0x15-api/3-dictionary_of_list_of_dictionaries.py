#!/usr/bin/python3
"""returns info about TODO list progress for given employee id"""
import json
import requests
from sys import argv


def gen_dict(user_id):
    username = ((requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            user_id))).json()).get('username')
    todos = (requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            user_id))).json()

    return ([{"username": username,
              "task": todo.get('title'),
              "completed": todo.get('completed')
              }
            for todo in todos])


if __name__ == '__main__':
    users = [user.get('id') for user in requests.get(
        'https://jsonplaceholder.typicode.com/users').json()]
    todo_all_employees_dict = {
        user_id: gen_dict(user_id) for user_id in users}
    print(todo_all_employees_dict)
    # with open('todo_all_employees', 'w') as f:
    #    json.dump(todo_all_employees_dict, f)
