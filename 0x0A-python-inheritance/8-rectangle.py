#!/usr/bin/python3

"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer_validator method"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return (value)


"""BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """__init__ constructor method"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
