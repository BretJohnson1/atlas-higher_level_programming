#!/usr/bin/python3
import string
for letter in string.ascii_lowercase:
    print(letter.format(string.ascii_lowercase), end=' ')
