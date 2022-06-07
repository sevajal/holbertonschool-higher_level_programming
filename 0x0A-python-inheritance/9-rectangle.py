#!/usr/bin/python3

"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer_validator method"""
        self.name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be a int")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value


"""BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """__init__ constructor method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area method"""
        return self.__width * self.__height

    def print(self):
        """Print method"""
        width = self.__width
        height = self.__height
        print(f"[Rectangle] {width}/{height}")

    def __str__(self):
        """__str__ method"""
        width = str(self.__width)
        height = str(self.__height)
        result = "[Rectangle] " + width + "/" + height
        return result
