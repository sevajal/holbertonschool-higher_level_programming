#!/usr/bin/python3

"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0):
        """__init__ constructor method: creates a square object.
        args: size - size of the square."""
        self.size = size

    def area(self):
        """Return the square area"""
        return (self.__size ** 2)

    def my_print(self):
        """ prints in stdout the square with the character #"""
        if self.__size > 0:
            i = 0
            while i < self.__size:
                y = 0
                while y < self.__size:
                    print("#", end="")
                    y += 1
                print()
                i += 1
        else:
            print()

    @property
    def size(self):
        """Retrieve the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the square size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
