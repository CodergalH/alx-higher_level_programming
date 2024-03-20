#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argn = len(argv)

    if argn > 1:
        print("{:d} arguements:".format(argn))
    elif argn == 1:
        print("{:d} argument:".format(argn))
    else:
        print("0 arguement.")

    for i in range(argn):
        print("{:d}: {}".format(i + 1, argv[i]))
