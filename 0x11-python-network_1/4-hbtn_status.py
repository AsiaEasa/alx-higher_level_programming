#!/usr/bin/python3
import requests

def main():
    URL = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(URL)
    
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

if __name__ == "__main__":
    main()
