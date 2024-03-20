#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    namelist = dir(hidden_4)

    sortedlist = [i for i in namelist if i.startswith("__") is False]

    for i in sortedlist:
        print("{}".format(i))
