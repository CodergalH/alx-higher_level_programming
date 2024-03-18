#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        lena = len(tuple_a)
        lenb = len(tuple_b)

        if (lena < 2 or lenb < 2):
            if lena == 1:
                a1 = tuple_a[0]
                a2 = 0
            elif lena == 0:
                a1 = 0
                a2 = 0

            if lenb == 1:
                b1 = tuple_b[0]
                b2 = 0
            elif lenb == 0:
                b1 = 0
                b2 = 0
        else:
            a1 = tuple_a[0]
            a2 = tuple_a[1]
            b1 = tuple_b[0]
            b2 = tuple_b[1]

        new_tuple = (a1 + b1, a2 + b2)
        return new_tuple
