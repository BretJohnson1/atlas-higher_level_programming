#!/usr/bin/python3
"""This file defines a function that prints after characters"""


def text_indentation(text):
    """This function prints after special characters"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_line = True
    for char in text:
        if char != ' ' or new_line is False:
            print(char, end='')
            new_line = False
        elif char != ' ':
            new_line = False
        if char in ['.', '?', ':']:
            print()
            print()
            new_line = True
