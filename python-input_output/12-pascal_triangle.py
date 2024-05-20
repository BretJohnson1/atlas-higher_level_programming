#!/usr/bin/python3
"""
This module defines a function that populates lists for pascal's triangle
"""


def pascal_triangle(n):
    """This function populates lists for pascal's triangle"""
    if n <= 0:
        my_list = []
        return my_list

    new_list = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = new_list[i - 1][j - 1] + new_list[i - 1][j]
        new_list.append(row)
    return new_list
