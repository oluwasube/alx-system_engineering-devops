#!/usr/bin/python3
"""query REDDIT API and returns the number of subsrcibers"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subcribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    custom_headers = {
               "User-Agent":
               "ubuntu4.20:0x16-api:v1.0.0 (by /u/oluwasube)"
              }
    try:
        response = requests.get(url,
                                headers=custom_headers,
                                allow_redirects=False).json()
        return response["data"]["subscribers"]
    except Exception:
        return 0
