#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dictionary2 = a_dictionary
    alist = list(a_dictionary2)

    for i in alist:
        if a_dictionary2[i] == value:
            a_dictionary2.pop(i)

    return a_dictionary2
