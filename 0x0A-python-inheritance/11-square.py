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

    def print(self):
        """Print method"""
        size = self.__size
        print(f"[Square] {size}/{size}")

    def __str__(self):
        """__str__ method"""
        size = str(self.__size)
        result = "[Square] " + size + "/" + size
        return result
