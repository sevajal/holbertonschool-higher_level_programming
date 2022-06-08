#!/usr/bin/python3

"""Function add_attribute"""


def add_attribute(object, attribute, value):
    """Function add_attribute"""
    if hasattr(object, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(object, attribute, value)
