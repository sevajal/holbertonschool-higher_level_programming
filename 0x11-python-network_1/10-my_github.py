#!/usr/bin/python3
'''Script that takes my GitHub credentials (username and password)
and uses the GitHub API to display my id'''
import requests
import sys

if __name__ == "__main__":
    try:
        r = requests.get('https://api.github.com/user',
                         auth=requests.auth.HTTPBasicAuth(sys.argv[1],
                                                          sys.argv[2]))
        print(r.json()['id'])
    except:
        print("None")
