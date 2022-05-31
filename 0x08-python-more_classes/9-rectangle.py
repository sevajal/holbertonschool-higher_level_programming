#!/usr/bin/python3

"""Rectangle module"""


class Rectangle:
    """Class that defines a rentangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Constructor Method __init___"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def print(self):
        """Print Method that prints the rectangle with the char #"""
        width = self.__width
        height = self.__height
        if width > 0 and height > 0:
            [print(width * str(self.print_symbol)) for x in range(height)]
        else:
            print()

    def __str__(self):
        """__str__ Method that returns the rectangle as a string"""
        result = ""
        width = self.__width
        height = self.__height
        if width > 0 and height > 0:
            for x in range(height - 1):
                result += width * str(self.print_symbol) + "\n"
            result += width * str(self.print_symbol)
            return result
        else:
            return result

    def __repr__(self):
        """__repr__ Method returns the internal representation of an object"""
        width = self.__width
        height = self.__height
        result = "Rectangle(" + str(width) + ", " + str(height) + ")"
        return result

    def __del__(self):
        """__del__ Method deletes an object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static Method to compare to rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        """Class Method that returns a new rectangle"""
        square = Rectangle(size, size)
        return square
