#!/usr/bin/python3

"""Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """__init__ constructor method"""
        self.integer_validator("size", size)
        self.__size = size
        self._Rectangle__width = size
        self._Rectangle__height = size

    def area(self):
        """Area method"""
        return self.__size ** 2
