#!/usr/bin/python3
def remove_char_at(str, n):
    if (str == "" or n >= len(str) - 1):
        return str
    str_cpy = str

    str_cpy = str_cpy.replace(str_cpy[n], '')

    return str_cpy
