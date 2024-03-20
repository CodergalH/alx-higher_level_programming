#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    cpy = argv
    argn = len(cpy)

    print("{:d} ".format(argn - 1), end="")
    if argn > 2:
        print("arguments:")
        for i in range(1, argn):
            print("{:d}: {}".format(i, cpy[i]))
    elif argn == 1:
        print("arguments.")
    elif argn == 2:
        print("argument:")
        for i in range(1, argn):
            print("{:d}: {}".format(i, cpy[i]))
    else:
        print()
