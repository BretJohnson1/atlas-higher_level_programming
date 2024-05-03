#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for key in a_dictionary:
        new_dictionary[key] += new_dictionary[key]
        return new_dictionary
