#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    cpy = sys.argv
    argn = len(cpy)

    print("{:d} ".format(argn), end="")
    if argn == 1:
        print("argument:")
    elif argn == 0:
        print("arguements.")
    else:
        print("arguments:")

    for i in range(argn):
        print("{:d}: {}".format(i + 1, cpy[i]))
