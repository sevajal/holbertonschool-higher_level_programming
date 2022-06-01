#!/usr/bin/python3

"""0-add_integer module that contain the function add_integer"""


def add_integer(a, b=98):
    """function that returns the add of two integers"""
    if not a or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if not b or type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
