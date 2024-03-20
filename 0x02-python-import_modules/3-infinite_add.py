#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argn = len(sys.argv)
    result = 0
    if argn > 2:
        for i in range(1, argn):
            result += int(argn[i])
    elif argn == 2:
        result = int(argn[1])
    else:
        result = 0

    print("{:d}".format(result))
