#!/usr/bin/python3
"""
Reterive information about his/her todo list progres
for a given employee ID
"""


import requests
import sys


if __name__ == '__main__':
    args = int(sys.argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(args))
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    data_todo = todo.json()
    name = user.json().get('name')
    new_list = [i for i in data_todo if i.get("userId") == args]
    total_task = len(new_list)
    done = [i for i in new_list if i.get('completed') is True]
    done_task = len(done)
    print(f'Employee {name} is done with tasks({done_task}/{total_task}):')
    for title in done:
        print(f"\t {title.get('title')}")
