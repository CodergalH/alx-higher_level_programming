#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        uniq = set(my_list)
        uniq_list = list(uniq)

        result = sum(uniq_list)

        return result
