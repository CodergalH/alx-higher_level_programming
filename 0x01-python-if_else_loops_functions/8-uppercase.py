#!/usr/bin/python3

def uppercase(str):
    index = len(str)

    if str == "":
        str = str + " "
        index += 1

    for element in range(0, index):

        char_num = ord(str[element])

        if (char_num >= 97 and char_num <= 122):
            char_num -= 32

        print("{:c}".format(char_num), end="")

        if (element == index - 1):
            print()
