#!/usr/bin/python3
"""Export data in JSON format"""
import json
import requests
import sys
import urllib


def singleRecordJson(url, userId):
    """export single record to json format"""
    user = requests.get(url + "/users/{}".format(userId)).json()
    todos = requests.get(url + "/users/{}/todos/".format(userId)).json()
    username = user.get("username")
    tasks = []
    for task in todos:
        task_dic = {}
        task_dic["task"] = task.get("title")
        task_dic["completed"] = task.get("completed")
        task_dic["username"] = username
        tasks.append(task_dic)
    return tasks


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url + "/users/").json()
    dic = {}
    for user in users:
        dic[user.get("id")] = singleRecordJson(url, user.get("id"))
    with open("todo_all_employees.json", "w") as alljsonfile:
        json.dump(dic, alljsonfile)
