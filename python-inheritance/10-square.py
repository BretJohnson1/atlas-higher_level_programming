#!/usr/bin/python3
"""This module defines a class named Square that is inherited"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This defines a class names Square that is inherited"""

    def __init__(self, size):
        """This defines the public instantation method"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
