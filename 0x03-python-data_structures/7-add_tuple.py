#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    a1 = tuple_a[0]
    a2 = tuple_a[1]
    b1 = tuple_b[0]
    b2 = tuple_b[1]

    new_tuple = (a1 + b1, a2 + b2)
    return new_tuple
