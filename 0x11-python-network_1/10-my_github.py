#!/usr/bin/python3
"""
Uses the GitHub API with Basic Authentication to display the user id.
"""
import requests
import sys

if __name__ == "__main__":
    USER = sys.argv[1]
    PASS = sys.argv[2]

    URL = 'https://api.github.com/user'
    res = requests.get(URL, auth=(USER, PASS))

    if res.status_code == 200:
        user_in = res.json()
        user_id = user_in.get('id')
        print(user_id)
    else:
        print("None")
