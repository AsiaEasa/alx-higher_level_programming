#!/usr/bin/python3
"""Python script that sends a request to the URL and
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    M = requests.get(url)
