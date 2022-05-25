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

    def __lt__(self, other):
        """Compare if a square is smaller than other"""
        return (self.__size < other.__size)

    def __le__(self, other):
        """Compare if a square is smaller or equal than other"""
        return (self.__size <= other.__size)

    def __gt__(self, other):
        """Compare if a square is bigger than other"""
        return (self.__size > other.__size)

    def __ge__(self, other):
        """Compare if a square is bigger or equual than other"""
        return (self.__size >= other.__size)

    def __eq__(self, other):
        """Compare if two squares are equal"""
        return (self.__size == other.__size)

    def __ne__(self, other):
        """Compare if two squares are not equal"""
        return (self.__size != other.__size)
