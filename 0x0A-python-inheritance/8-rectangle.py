#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""Rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """__init__ constructor method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
