#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= char <= 122:
            char = char(ord(char) - 32)
            print("{}".format(char), end="")
            print("")
