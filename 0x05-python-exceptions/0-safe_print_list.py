#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ret = 0
        for i in range(x):
            print(my_list[i], end="")
            ret += 1
        print(end='\n')  # Add a newline
    except IndexError:
        pass
    return ret