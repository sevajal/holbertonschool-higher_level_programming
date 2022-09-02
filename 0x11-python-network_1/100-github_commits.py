#!/usr/bin/python3
'''Script that list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”'''
import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits',
    auth=requests.auth.HTTPBasicAuth('sevajal', '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'))
    print(r.text)
