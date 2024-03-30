#!/usr/bin/python3
"""script that fetches"""
import urllib.request

def main():
    url = 'https://alx-intranet.hbtn.io/status'

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))

if __name__ == "__main__":
    main()
