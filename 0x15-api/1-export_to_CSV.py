#!/usr/bin/python3
""""
export data in the CSV format
"""

import csv
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
        entery.pop('id')
        entery["username"] = username
        formated_list.append(entery)
    fields = ["userId", "username", "completed", "title"]
    with open(f'{userId}.csv', 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
        csv_writer.writerows(formated_list)
