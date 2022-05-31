#!/usr/bin/python3

"""Rectangle module"""


class Rectangle:
    """Class that defines a rentangle"""
    def __init__(self, width=0, height=0):
        """Constructor Method __init___"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter Method for width instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter Method for width instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter Method for height instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter Method for height instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area Method that returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter Method that returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
