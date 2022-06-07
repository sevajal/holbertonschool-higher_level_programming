#!/usr/bin/python3

"""MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, value):
        """__init__ method"""
        self.__value = value

    def __eq__(self, other):
        """__eq__ method"""
        return (self.__value != other)

    def __ne__(self, other):
        """__ne__ method"""
        return (self.__value == other)
