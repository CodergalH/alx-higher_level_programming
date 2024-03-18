#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        j = 0
        newlist = []
        for i in my_list:
            if i % 2 == 0:
                newlist[j] = True
            else:
                newlist[j] = False
            j += 1

        return newlist
