#!/usr/bin/python3
def rev_alphabet():
    for i in range(122, 98, -1):
        if (i % 2) != 0:
            i -= 32

        print("{:c}".format(i), end="")
