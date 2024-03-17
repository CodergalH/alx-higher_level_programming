#!/usr/bin/python3

num = 0
while num < 10:
    num1 = num + 1
    for i in range((num1), 10):
        if (num == 8 and i == 9):
            print("{}{}".format(num, i))
            continue

        print("{}{}, ".format(num, i), end="")

    num += 1
