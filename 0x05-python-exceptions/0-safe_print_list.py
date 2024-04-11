#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print(end='\n')  # Add a newline
    except IndexError:
        pass
    return i + 1