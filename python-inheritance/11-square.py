#!/usr/bin/python3
"""This module defines a class named Square that is inherited"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a class named Square that is inherited"""

    def __init__(self, size):
        """This method is the public instantation method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """This method returns the string represenattion of a square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
