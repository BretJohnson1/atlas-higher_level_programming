#!/usr/bin/python3
"""This module contains a class defined as Rectangle"""


class Rectangle:
    """This is a class that defines a Rectangle"""
    def __init__(self, width=0, height=0):
        """This method initializes its properties"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """This method defines its width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This method sets value to its width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This method defines its height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This method sets value to its height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This public method returns the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """This public method returns the perimeter of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """This method is the string representation of the Rectangle"""
        string = ""
        if self.width > 0 and self.height > 0:
            for row in range(self.height):
                for col in range(self.width):
                    string += '#'
                if row < self.height - 1:
                    string += '\n'
            return string
        else:
            return string
