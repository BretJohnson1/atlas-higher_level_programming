#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newList = []
    len_list = len(my_list)
    for index in range(len_list):
        if my_list[index] % 2 == 0:
            newList.append(True)
        else:
            newList.append(False)
            return newList
