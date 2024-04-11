#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ret = 0
    try:
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                ret += 1
            else:
                i += 1
        print(end="\n")
    except (IndexError, TypeError):
        print(end="")
    return ret
