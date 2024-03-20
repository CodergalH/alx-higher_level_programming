#!/bin/usr/python3
if __name__ == "__main__":
    import sys

    argn = len(sys.argv)
    print("{:d} ".format(argn - 1), end="")

    if argn > 2:
        print("arguments:")
    elif argn == 2:
        print("argument:")
    else:
        print("argument.")

    for i in range(1, argn):
        print("{:d}: {}".format(i, sys.argv[i]))
