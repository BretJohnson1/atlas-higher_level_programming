#!/usr/bin/python3
"""For my square"""


class Square:
    """ Initializing Class for my square."""
    def __init__(self, size=0):
        """ New sqaure


        Args:
        size (int): Size of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
