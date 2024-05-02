#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        last_element = row[-1]
        for element in row:
            if element != last_element:
                print("{:d} ".format(element), end='')
            else:
                print("{;d}".format(element), end='')
                print()
