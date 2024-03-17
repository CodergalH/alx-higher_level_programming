#!/usr/bin/python3

def uppercase(str):
    index = len(str)

    for element in range(0, index):
        char_num = ord(str[element])

        if (element == index - 1):
            if (char_num >= 97 and char_num <= 122):
                char_num -= 32
            print("{:c}".format(char_num))
            continue

        if (char_num >= 97 and char_num <= 122):
            char_num -= 32

        print("{:c}".format(char_num), end="")
