#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    my_list.sort()
    ret = my_list[len(my_list) - 1]
    return ret
