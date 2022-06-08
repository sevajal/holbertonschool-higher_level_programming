#!/usr/bin/python3

"""class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object"""
    my_dict = {}
    if hasattr(obj, "__dict__"):
        my_dict = obj.__dict__
    return my_dict
