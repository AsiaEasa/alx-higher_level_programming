#!/usr/bin/env python3
import urllib.request
import urllib.error
import sys

def main():
    URL = sys.argv[1]

    try:
        with urllib.request.urlopen(URL) as res:
            B = res.read().decode('utf-8')
            print(B)
    except urllib.error.HTTPError as E:
        print(f"Error code: {E.code}")

if __name__ == "__main__":
    main()
