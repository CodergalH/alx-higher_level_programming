#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        j = 0
        newlist = []
        for i in my_list:
            newlist[j] = print(i % 2 == 0)
            j += 1
        return newlist
