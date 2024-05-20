#!/usr/bin/python3
"""This module defines a function that writes to a file"""


def write_file(filename="", text=""):
    """
    This function writes to a file and returns the number of new chars
    """
    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
