#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        type = isinstance(mylist[i], int)
        if type != True:
            continue
        print("{}".format(my_list[i]))
