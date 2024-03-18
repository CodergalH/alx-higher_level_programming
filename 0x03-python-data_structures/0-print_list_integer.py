#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        type = isinstance(my_list[i], int)
        if type is not True:
            continue
        print("{}".format(my_list[i]))
