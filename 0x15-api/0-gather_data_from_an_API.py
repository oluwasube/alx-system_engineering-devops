#!/usr/bin/python3
"""Return information about the TODO list progress for a given employee ID"""
import requests
import sys
import urllib


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/users/{}/todos/".format(sys.argv[1])).json()
    total_tasks = len(todos)
    complete_tasks = []
    for task in todos:
        if task.get("completed"):
            complete_tasks.append(task.get("title"))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get("name"), len(complete_tasks), total_tasks))
    for complete_task in complete_tasks:
        print("\t {}".format(complete_task))
