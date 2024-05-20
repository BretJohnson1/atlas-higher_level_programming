#!/usr/bin/python3
""" This module defines a class MyList that inherits from list"""


class MyList(list):
    """ This is a class MyList that inherits from list"""

    def print_sorted(self):
        """ This method prints a sorted list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
