#!/usr/bin/python3
"""This module defines a class Rectangle that is inherited"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This defines a class Rectangle that is inherited"""
    def __init__(self, width, height):
        """Instantiation method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This defines a method that returns the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This method returns the string representation of Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)