#!/usr/bin/python3

"""save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file
    using a JSON representation"""
    import json
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
