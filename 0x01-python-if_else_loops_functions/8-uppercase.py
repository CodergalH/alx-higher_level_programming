#!/usr/bin/python3

def uppercase(str):
    index = len(str)

    for element in str:
        char_num = ord(element)

        if (element == str[index - 1]):
            if (char_num >= 97 and char_num <= 122):
                char_num -= 32
            print("{:c}".format(char_num))
            continue

        if (char_num >= 97 and char_num <= 122):
            char_num -= 32

        print("{:c}".format(char_num), end="")
