#!/usr/bin/python3

"""load_from_json_file function"""


def load_from_json_file(filename):
    """Function that creates an Object from a “JSON file"""
    import json
    with open(filename, encoding="utf-8") as file:
        return json.loads(file.read())
