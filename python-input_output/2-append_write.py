#!/usr/bin/python3
"""This module defines a function that appends a string to a file"""


def append_write(filename="", text=""):
    """
    This function appends a string to the end of a file
    and returns the characters written
    """
    with open(filename, mode='a', encoding="utf-8") as f:
        return f.write(text)
