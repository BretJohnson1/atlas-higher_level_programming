#!/usr/bin/python3
def squareit(number):
    result = number ** 2
    return result


def square_matrix_simple(matrix=[]):
    newMatrix = [list(map(squareit, row)) for row in matrix]
    return newMatrix
