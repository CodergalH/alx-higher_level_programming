#!/usr/bin/python3

def uppercase(str):
    for element in str:
        char_num = ord(element)
        if (char_num >= 97 and char_num <= 122):
            char_num -= 32
            print("{:c}".format(char_num), end="")
        else:
            print("{:c}".format(char_num), end="")

    print()
