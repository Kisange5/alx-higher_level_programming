#!/usr/bin/python3
"""module documentation"""


class Rectangle:
    """a class rep for a rectangle
    Args:
        width (int): the size of width
        height (int): the size of the width
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            value (int): the value to set to
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value (int): the value to set to
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area of the rectangle
        Return:
              area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculates perimeter of the rectangle
        Return:
              perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """prints the rectangle with '#' character
        Return:
              an empty string if height/width is 0
              else
              the rectangle made up of '#'
        """
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        else:
            t = 0
            for i in range(self.__height):
                for j in range(self.__width):
                    rec += '#'
                t += 1
                if t != self.__height:
                    rec += '\n'
            return rec

    def __repr__(self):
        """returns the repr of the instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """deletes the instance of the rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
