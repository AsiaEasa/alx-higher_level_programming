#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    URL = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}

    res = requests.post(URL, data=payload)

    try:
        json_res = res.json()
        if json_res:
            print("[{}] {}".format(json_res['id'], json_res['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
