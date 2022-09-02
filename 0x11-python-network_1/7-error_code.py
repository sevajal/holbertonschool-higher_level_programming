#!/usr/bin/python3
'''script that takes in a URL, sends a request to the URL and displays
the body of the response.'''
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    code = r.status_code
    if code >= 400:
        print(f'Error code: {code}')
    else:
        print(r.text)
