#!/usr/bin/python3
import urllib.request
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    URL = sys.argv[1]

    REQ = urllib.request.Request(URL)

    with urllib.request.urlopen(REQ) as res:
        x_request_id = res.headers.get('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    main()
