#!/usr/bin/python3
"""
Sends a request to the given URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, prints an error message.
"""
import requests
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    res = requests.get(URL)

    if res.status_code >= 400:
        print("Error code:", res.status_code)
    else:
        print(res.text)
