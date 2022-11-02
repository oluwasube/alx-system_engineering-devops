#!/usr/bin/python3
"""Export data in JSON format"""
import json
import requests
import sys
import urllib


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "/users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "/users/{}/todos/".format(sys.argv[1])).json()
    username = user.get("username")
    dic = {}
    tasks = []
    with open("{}.json".format(sys.argv[1]), "w") as jsonfile:
        for task in todos:
            task_dic = {}
            task_dic["task"] = task.get("title")
            task_dic["completed"] = task.get("completed")
            task_dic["username"] = username
            tasks.append(task_dic)
        dic[sys.argv[1]] = tasks
        json.dump(dic, jsonfile)
