#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    for i in my_list:
        num = my_list.index(i)
        newlist.insert(num, i % 2 == 0)
    return newlist
