#!/usr/bin/python3
'''script that fetches https://intranet.hbtn.io/status'''
import requests

if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    r = r.text
    print("Body response:")
    print(f"\t- type: {type(r)}")
    print(f"\t- content: {r}")
