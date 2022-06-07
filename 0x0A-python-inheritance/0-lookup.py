#!/usr/bin/python3

"""Function lookup"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object"""
    return list(dir(obj))
