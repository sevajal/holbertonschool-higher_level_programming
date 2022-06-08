#!/usr/bin/python3

"""Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def __str__(self):
        """__str__ method"""
        width = str(self.__width)
        height = str(self.__height)
        result = "[Rectangle] " + width + "/" + height
        return result


"""Square class"""


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
