#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """__init__ constructor method: creates a square object.
        args: size - size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
