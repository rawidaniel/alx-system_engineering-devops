#!/usr/bin/python3
"""
export data in the JSON format
"""

import json
import requests
import sys


if __name__ == '__main__':
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    username = user.json().get('username')
    todo = requests.get('https://jsonplaceholder.typicode.com/todos')
    new_list = [i for i in todo.json() if i.get("userId") == int(userId)]
    formated_list = []
    for entery in new_list:
        if entery.get('userId') == int(userId):
            new_dict = {}
            new_dict['task'] = entery['title']
            new_dict['completed'] = entery['completed']
            new_dict['username'] = username
            formated_list.append(new_dict)
    dict_new = {f'{userId}': formated_list}
    with open(f"{userId}.json", 'w') as write_file:
        json.dump(dict_new, write_file)
